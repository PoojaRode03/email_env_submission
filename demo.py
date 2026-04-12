
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from env.environment import EmailEnv
from env.models import Action

print("Running demo...")

env = EmailEnv()
obs = env.reset()

print("Initial State:", obs)

action = Action(action_type="classify", email_id=1, value="spam")
action = Action(action_type="prioritize", email_id=2, value="high")

obs, reward, done, _ = env.step(action)

print("After Step:", obs)
print("Reward:", reward)