import os, time
import gymnasium as gym
from gymnasium.wrappers import RecordVideo
from stable_baselines3 import PPO

ENV_ID = "BipedalWalker-v3"

def record(model_path="ppo_bipedal_walker.zip"):
    run_name = time.strftime("%Y-%m-%d_%H%M%S")
    video_folder = os.path.join("recordings", run_name)
    os.makedirs(video_folder, exist_ok=True)

    env = gym.make(ENV_ID, render_mode="rgb_array")

    env = RecordVideo(
        env,
        video_folder=video_folder,
        name_prefix=f"bipedal_eval_{run_name}",
        episode_trigger=lambda ep: ep == 0
    )

    model = PPO.load(model_path, env=env)

    obs, _ = env.reset()

    done = False
    while not done:
        env.render()  # IMPORTANT: ensure frames are captured
        action, _ = model.predict(obs, deterministic=True)
        obs, _, terminated, truncated, _ = env.step(action)
        done = terminated or truncated

    env.close()
    print("Saved video to:", video_folder)


