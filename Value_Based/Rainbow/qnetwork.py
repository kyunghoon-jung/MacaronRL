import torch
import numpy as np
import torch.nn as nn
import torch.optim as optim 
import torch.nn.functional as F 

class Noisy_LinearLayer(nn.Module):
    ''' Noisy linear layer '''
    def __init__(self, 
                input_feature: "int: the number of input features", 
                output_feature: "int: the number of output features", 
                initial_std: "float: the standard daviation used for parameter initialization"):

        super(Noisy_LinearLayer, self).__init__()

        self.input_feature = input_feature
        self.output_feature = output_feature
        self.init_noise_std = initial_std

        # nn.Parameter : this is learnable parameters. Set by default as "requires_grad=True" 
        self.weight_mu_params = nn.Parameter(torch.Tensor(output_feature, input_feature))
        self.weight_sigma_params = nn.Parameter(torch.Tensor(output_feature, input_feature))
        self.bias_mu_params = nn.Parameter(torch.Tensor(output_feature))
        self.bias_sigma_papams = nn.Parameter(torch.Tensor(output_feature))

        # register_buffer : this is not learnable variable. self.weight_epsilon = torch.Tensor(43,
        self.register_buffer(
            "weight_epsilon", torch.Tensor(output_feature, input_feature)
            )
        self.register_buffer(
            "bias_epsilon", torch.Tensor(output_feature)
        )

        self.initialize_parameters()
        self.initialize_factorized_noise()

    def initialize_parameters(self):
        """Initialize weights and biases w.r.t. the case of using factorized gaussian noise"""
        params_range = 1 / np.sqrt(self.input_feature)
        self.weight_mu_params.data.uniform_(-params_range, params_range)
        self.bias_mu_params.data.uniform_(-params_range, params_range)

        self.weight_sigma_params.data.fill_(self.init_noise_std/np.sqrt(self.input_feature))
        self.bias_sigma_papams.data.fill_(self.init_noise_std/np.sqrt(self.input_feature))

    def initialize_factorized_noise(self):
        """Initialize noise parameters with unit gaussian dist. in factorized way"""
        eps_in = torch.randn(self.input_feature)
        eps_in = eps_in.sign() * eps_in.abs().sqrt()
        eps_out = torch.randn(self.output_feature)
        eps_out = eps_out.sign() * eps_out.abs().sqrt()
        self.weight_epsilon.copy_(eps_out.ger(eps_in))
        self.bias_epsilon.copy_(eps_out)

    def forward(self, x):
        """ F.linear passes input x with linear computation """
        return F.linear(x, self.weight_mu_params + self.weight_sigma_params*self.weight_epsilon,
                        self.bias_mu_params + self.bias_sigma_papams*self.bias_epsilon)
                        
class QNetwork(nn.Module):
    
    def __init__(self, input_dim, action_dim, initial_std, rand_seed=False,
                conv_channel_1=32, conv_channel_2=64, conv_channel_3=64,
                kernel_1=8, kernel_2=4, kernel_3=3, 
                stride_1=4, stride_2=2, stride_3=1,
                linear_1=512, linear_2=512, n_atoms=51):

        super(QNetwork, self).__init__()
        self.action_dim = action_dim
        self.n_atoms = n_atoms
        # self.seed = torch.manual_seed(rand_seed)
        self.Conv1 = nn.Conv2d(input_dim[0], conv_channel_1, (kernel_1,kernel_1), stride=stride_1)
        self.Conv2 = nn.Conv2d(conv_channel_1, conv_channel_2, (kernel_2,kernel_2), stride=stride_2)
        self.Conv3 = nn.Conv2d(conv_channel_2, conv_channel_3, (kernel_3,kernel_3), stride=stride_3)

        def calculate_conv2d_size(size, kernel_size, stride):
            return (size - (kernel_size - 1) - 1) // stride  + 1

        w, h = input_dim[1], input_dim[2]
        convw = calculate_conv2d_size(calculate_conv2d_size(calculate_conv2d_size(w,kernel_1,stride_1),
                                                            kernel_2,stride_2),
                                      kernel_3,stride_3)
        convh = calculate_conv2d_size(calculate_conv2d_size(calculate_conv2d_size(h,kernel_1,stride_1),
                                                            kernel_2,stride_2),
                                      kernel_3,stride_3)
        linear_input_size = convw * convh * conv_channel_3

        # Noisy Linear Layers
        self.V_noisy_linear1 = Noisy_LinearLayer(linear_input_size, linear_1, initial_std) 
        self.V_noisy_linear2 = Noisy_LinearLayer(linear_1, n_atoms, initial_std) # Dist. of Values
        self.A_noisy_linear1 = Noisy_LinearLayer(linear_input_size, linear_2, initial_std) 
        self.A_noisy_linear2 = Noisy_LinearLayer(linear_2, action_dim*n_atoms, initial_std) # Dist. of Action-Values

        self.relu = nn.ReLU()

    def forward(self, x):
        
        x = self.relu(self.Conv1(x)) 
        x = self.relu(self.Conv2(x)) 
        x = self.relu(self.Conv3(x)) 
        x = x.reshape(x.shape[0], -1) 
        V = self.V_noisy_linear2(self.relu(self.V_noisy_linear1(x))).view(-1, 1, self.n_atoms) 
        A = self.A_noisy_linear2(self.relu(self.A_noisy_linear1(x))).view(-1, self.action_dim, self.n_atoms)

        Q = V + A - A.mean(dim=1, keepdim=True) 
        return F.softmax(Q, dim=-1) # Shape: (batch_size, action_dim, n_atoms)

    def init_noise(self):

        self.V_noisy_linear1.initialize_factorized_noise()
        self.V_noisy_linear2.initialize_factorized_noise()
        self.A_noisy_linear1.initialize_factorized_noise()
        self.A_noisy_linear2.initialize_factorized_noise()
