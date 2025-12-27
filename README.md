# Bipedal-Walker with Reinforcement Learning (PPO)
This repository contains my implementation of a reinforcement learning agent for the BipedalWalker-v3 environment using the PPO. 

It contains the training code (train.ipynb) which contains all the experiments, final GIFs, and almost everything needed to successfully implement the agent. The repo also has record.py (a supporting file) which is used to record videos of the agent. Apart from these code files, I posted my agent's GIFs at different stages of the process along with the final video of the walker "Final_Bipedal_Walker.mp4". The repo contains a csv file with the statistics of different entropy coefficients. These stats were pivotal for the execution of the walker.

This is my first RL project, and the goal was to see how different development choices influences learning rate, stability and performance of the final model. This repo contains everything that's needed to reprdouce this experiment. The files needed for conducting this experiment is train.ipynb and record.py. Everything else is automatically generated during the execution of the luck.

A quick highlight of the results over 100 runs:
------------------------------------------
Mean: 300.99
Std: 46.86
Median: 311.73
20th percentile: 310.46
80th percentile: 313.14
Fail rate (<200): 0.06
------------------------------------------

This project formally passes the BipedalWalker - v3.

**References**
Schulman, J., Wolski, F., Dhariwal, P., Radford, A., & Klimov, O. (2017). Proximal Policy Optimization Algorithms. arXiv preprint arXiv:1707.06347. https://arxiv.org/abs/1707.06347

Ioffe, S., & Szegedy, C. (2015). Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift. ICML. https://arxiv.org/abs/1502.03167

Henderson, P., Islam, R., Bachman, P., Pineau, J., Precup, D., & Meger, D. (2018). Deep reinforcement learning that matters. Proceedings of the AAAI Conference on Artificial Intelligence, 32(1). https://arxiv.org/abs/1709.06560

