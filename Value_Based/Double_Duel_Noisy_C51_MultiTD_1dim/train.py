import torch
import torch.nn as nn
import torch.optim as optim 
import torch.nn.functional as F 
from torchsummary import summary
from subprocess import call
import numpy as np
import time    
import gym    
import cv2
import os

from agent import Agent
from replay_buffer import ReplayBuffer
from qnetwork import QNetwork 
import matplotlib.pyplot as plt
from IPython.display import clear_output
import wandb   
from subprocess import call

env_list = {
    0: "CartPole-v0",
    1: "CartPole-v2",
    2: "LunarLander-v2",
    3: "Breakout-v4",
    4: "BreakoutDeterministic-v4",
    5: "BreakoutNoFrameskip-v4",
    6: "BoxingDeterministic-v4",
    7: "PongDeterministic-v4",
}
# env.seed(0)
env_name = env_list[2]
env = gym.make(env_name)
input_dim = env.observation_space.shape[0]
print("env_name", env_name) 
print(env.action_space.n) 

update_start_buffer_size = 5000
num_frames = 2000000

gamma = 0.99
buffer_size = int(100000) 
batch_size = 32           
update_type = 'hard'
soft_update_tau = 0.002
learning_rate = 0.0005
target_update_freq = 150
current_update_freq = 4 # Update frequency of current Q-Network.  

device_num = 0
rand_seed = None
rand_name = ('').join(map(str, np.random.randint(10, size=(3,))))
folder_name = os.getcwd().split('/')[-1] 

# NoisyNet Variable
initial_std = 0.5 

# Variables for Multi-step TD
n_step = 3

# Variables for Categorical RL
n_atoms = 51
Vmax = 600
Vmin = -600

project_name = 'rainbow-per'
model_number = 0
main_path = '/data3/Jungkh/RL/'
model_save_path = \
f'{rand_name}_{env_name}_tot_f:{num_frames}f\
_gamma:{gamma}_tar_up_frq:{target_update_freq}f\
_up_type:{update_type}_soft_tau:{soft_update_tau}f\
_batch:{batch_size}_buffer:{buffer_size}f\
_up_start:{update_start_buffer_size}_lr:{learning_rate}f\
_device:{device_num}_rand:{rand_seed}_{model_number}/'
if not os.path.exists(main_path):
    os.mkdir('./model_save/')
    model_save_path = './model_save/' + model_save_path
    if not os.path.exists(model_save_path):
        os.mkdir(model_save_path)
else:
    model_save_path = main_path + model_save_path
    if not os.path.exists(model_save_path):
        os.mkdir(model_save_path)
print("model_save_path:", model_save_path)

plot_option = 'wandb'
# plot_option = 'inline'
# plot_option = False

if plot_option=='wandb':
    call(["wandb", "login", "000c1d3d8ebb4219c3a579d5ae02bc38be380c70"])
    os.environ['WANDB_NOTEBOOK_NAME'] = 'RL_experiment'
    wandb.init(
            project=project_name,
            name=f"{rand_name}_{folder_name}_{env_name}",
            config={"env_name": env_name, 
                    "input_dim": input_dim,
                    "initial_std": initial_std,
                    "num_frames": num_frames,
                    "gamma": gamma,
                    "n_step": n_step,
                    "buffer_size": buffer_size,
                    "update_start_buffer_size": update_start_buffer_size,
                    "batch_size": batch_size,
                    "update_type": update_type,
                    "soft_update_tau": soft_update_tau,
                    "learning_rate": learning_rate,
                    "target_update_freq (unit:frames)": target_update_freq,
                    "current_update_freq (unit:frames)": current_update_freq,
                    "n_atoms": n_atoms,
                    "Vmax": Vmax,
                    "Vmin": Vmin
                    }
            )

agent = Agent( 
    env,
    input_dim,
    initial_std,
    num_frames,
    gamma,
    n_step,
    target_update_freq,
    current_update_freq,  
    update_type,
    soft_update_tau,
    batch_size,
    buffer_size,
    update_start_buffer_size,
    learning_rate,
    device_num,
    rand_seed,
    plot_option,
    model_save_path,
    n_atoms,
    Vmax,
    Vmin
) 

agent.train()