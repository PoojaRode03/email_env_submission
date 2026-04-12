# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

"""
Email Env Environment Implementation.

A simple test environment that echoes back messages sent to it.
Perfect for testing HTTP server infrastructure.
"""
#email_environment.py
from env.tasks import get_tasks
class Environment:
    pass
class EmailObservation:
    def __init__(self, observation, reward, done):
        self.observation = observation
        self.reward = reward
        self.done = done


class EmailEnvironment(Environment):

    def reset(self):
        return EmailObservation(
            observation="Environment reset",
            reward=0.3,
            done=False
        )

    def step(self, action):
        message = action.message.lower()
        task = action.task.lower()

        # TASK 1
        if task == "spam":
            if "win" in message or "lottery" in message:
                return EmailObservation("Spam detected", 0.83, True)
            return EmailObservation("Not spam", 0.27, True)

        # TASK 2
        elif task == "category":
            if "meeting" in message:
                return EmailObservation("Work email", 0.74, True)
            return EmailObservation("Other email", 0.41, True)

        # TASK 3
        elif task == "reply":
            return EmailObservation("Reply generated", 0.68, True)

        # fallback
        return EmailObservation("Invalid task", 0.19, True)

    def state(self):
        return {"status": "running"}

    def close(self):
        pass
    def get_task_list():
        return get_tasks()