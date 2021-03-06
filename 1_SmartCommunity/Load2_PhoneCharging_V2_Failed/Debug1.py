"""
Reinforcement learning maze example.

Red rectangle:          explorer.
Black rectangles:       hells       [reward = -1].
Yellow bin circle:      paradise    [reward = +1].
All other states:       ground      [reward = 0].

This script is the main part which controls the update method of this example.
The RL is in RL_brain.py.

View more on my tutorial page: https://morvanzhou.github.io/tutorials/
"""

from Home_env3 import HEMS_Env
from RL_brain import QLearningTable


def update():
    for episode in range(1000):
        # initial observation
        observation = env.reset()       # at the beginning, get the initial state of the episode.
        #env.render()
        while True:

            # RL take action and get next observation and reward
            action = RL.choose_action(observation)

            observation_, reward, done = env.step(action)
            #env.render()
            #print(env.count)
            RL.learn(observation, action, reward, observation_,  env.done)  # RL learn from this transition

            # swap observation

            env.S = observation_
            observation = observation_

            if done:
                break

    # end of game
    print('Game over')
    print(RL.q_table)
#   env.destroy()

if __name__ == "__main__":
    env = HEMS_Env()
    RL = QLearningTable(actions=env.action_space)
    update()
