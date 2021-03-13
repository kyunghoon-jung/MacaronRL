#### Welcome! This repo contains reinforcement learning algorithms.

- 2020.11.11 Confirmed for the performances of Value-based algorithms for several atari games such as Q-Bert, Breakout, Seaquest, Boxing, Pong, etc.

- 2021.02.15 Confirmed for the performances of Policy-based algorithms and distributed algorithms for CartPole and Lunarlander. 

- I'll write up the detailed comments in all the codes soon. 

- Colab online codes.
   - Value Based
      - DQN (1D Input) [![DQN](https://user-images.githubusercontent.com/56760035/110728455-749f4b80-8260-11eb-83bc-01f8dc29fdba.JPG)](https://colab.research.google.com/github/kyunghoon-jung/MacaronRL/blob/main/Value_Based/Vanila_DQN_1dim/Vanila_DQN_1dim%20input%20(simple%20atari%20game).ipynb)
      - DQN (2D Input) [![DQN](https://user-images.githubusercontent.com/56760035/110728455-749f4b80-8260-11eb-83bc-01f8dc29fdba.JPG)](https://colab.research.google.com/github/kyunghoon-jung/MacaronRL/blob/main/Value_Based/Vanila_DQN/Vanila_DQN_2dim%20input%20(same%20as%20DQN%20paper).ipynb)

   - Policy Based
      - REINFORCE in Discrete action space.  [![REINFORCE in Discrete action space](https://user-images.githubusercontent.com/56760035/110728455-749f4b80-8260-11eb-83bc-01f8dc29fdba.JPG)](https://colab.research.google.com/github/kyunghoon-jung/MacaronRL/blob/main/Policy_Based/REINFORCE/1.%20DiscreteREINFORCE.ipynb)

      - REINFORCE in Continuous action space.  [![REINFORCE in Continuous action space](https://user-images.githubusercontent.com/56760035/110728455-749f4b80-8260-11eb-83bc-01f8dc29fdba.JPG)](https://colab.research.google.com/github/kyunghoon-jung/MacaronRL/blob/main/Policy_Based/REINFORCE/2.%20ContinuousREINFORCE.ipynb)

      - REINFORCE with baseline in Discrete action space.  [![REINFORCE with baseline in Discrete action space](https://user-images.githubusercontent.com/56760035/110728455-749f4b80-8260-11eb-83bc-01f8dc29fdba.JPG)](https://colab.research.google.com/github/kyunghoon-jung/MacaronRL/blob/main/Policy_Based/REINFORCE/3.%20DiscreteREINFORCEwithBaseline.ipynb)

      - Actor-Critic in Discrete action space.  [![Actor Critic in Discrete action space](https://user-images.githubusercontent.com/56760035/110728455-749f4b80-8260-11eb-83bc-01f8dc29fdba.JPG)](https://colab.research.google.com/github/kyunghoon-jung/MacaronRL/blob/main/Policy_Based/Actor_Critic/4.%20DiscreteActorCritic.ipynb)

      - Actor-Critic in Continous action space.  [![Actor Critic in Continous action space](https://user-images.githubusercontent.com/56760035/110728455-749f4b80-8260-11eb-83bc-01f8dc29fdba.JPG)](https://colab.research.google.com/github/kyunghoon-jung/MacaronRL/blob/main/Policy_Based/Actor_Critic/5.%20ContinuousActorCritic.ipynb)

- Ray Pararell python package Totorial series.

   - Ray Tutorial  [![Ray_tutorial](https://user-images.githubusercontent.com/56760035/110728455-749f4b80-8260-11eb-83bc-01f8dc29fdba.JPG)](http://colab.research.google.com/github/kyunghoon-jung/MacaronRL/blob/main/Ray_tutorial/1.%20Ray_Simple_Turorial.ipynb)
   - Simple ReplayBuffer Tutorial [![ReplayBuffer](https://user-images.githubusercontent.com/56760035/110728455-749f4b80-8260-11eb-83bc-01f8dc29fdba.JPG)](colab.research.google.com/github/kyunghoon-jung/MacaronRL/blob/main/Ray_tutorial/2.%20Simple_ReplayBuffer_Tutorial.ipynb)
   - Simple ParameterServer Tutorial [![ParameterServer](https://user-images.githubusercontent.com/56760035/110728455-749f4b80-8260-11eb-83bc-01f8dc29fdba.JPG)](http://colab.research.google.com/github/kyunghoon-jung/MacaronRL/blob/main/Ray_tutorial/3.%20Simple_ParameterServer_Tutorial.ipynb)
   - Visualization with Ray Tutorial [![Visualization](https://user-images.githubusercontent.com/56760035/110728455-749f4b80-8260-11eb-83bc-01f8dc29fdba.JPG)](http://colab.research.google.com/github/kyunghoon-jung/MacaronRL/blob/main/Ray_tutorial/4.%20Visualization_with_Ray.ipynb)
   - Distributed DQN (with manipulating update steps)[![Distributed DQN manipulting](https://user-images.githubusercontent.com/56760035/110728455-749f4b80-8260-11eb-83bc-01f8dc29fdba.JPG)](http://colab.research.google.com/github/kyunghoon-jung/MacaronRL/blob/main/Ray_tutorial/5.%20Distributed_DQN_with_restricted_update_steps.ipynb)
   - Distributed DQN [![Distributed DQN](https://user-images.githubusercontent.com/56760035/110728455-749f4b80-8260-11eb-83bc-01f8dc29fdba.JPG)](http://colab.research.google.com/github/kyunghoon-jung/MacaronRL/blob/main/Ray_tutorial/6.%20Distributed_DQN.ipynb)


- References

    - Sutton - Reinforcement Learning Textbook 2nd ed.
    - https://github.com/Curt-Park/rainbow-is-all-you-need  
    - https://github.com/MrSyee/pg-is-all-you-need  
    - https://github.com/ShangtongZhang/DeepRL  
    - https://github.com/sfujim  
    - https://github.com/yandexdataschool/Practical_RL  
    - https://github.com/seungeunrho/minimalRL
