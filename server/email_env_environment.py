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
from openenv.core.env_server.interfaces import Environment
from openenv.core.env_server.types import State

from env.models import EmailAction, EmailObservation


class EmailEnvironment(Environment[EmailAction, EmailObservation, State]):

    def __init__(self):
        self._step_count = 0

    def reset(self, seed=None, episode_id=None, **kwargs):
        self._step_count = 0

        return EmailObservation(
            observation="Environment reset",
            reward=0.3,
            done=False
        )

    def step(self, action: EmailAction, timeout_s=None, **kwargs):
        self._step_count += 1

        message = action.message.lower()
        task = action.task.lower()

        if task == "spam":
            if "win" in message or "lottery" in message:
                result = "Spam detected"
                reward = 0.83
            else:
                result = "Not spam"
                reward = 0.27

        elif task == "category":
            if "meeting" in message:
                result = "Work email"
                reward = 0.74
            else:
                result = "Other email"
                reward = 0.41

        elif task == "reply":
            result = "Reply generated"
            reward = 0.68

        else:
            result = "Invalid task"
            reward = 0.19

        return EmailObservation(
            observation=result,
            reward=reward,
            done=True
        )

    @property
    def state(self):
        return State(
            episode_id="email-session",
            step_count=self._step_count
        )

    def close(self):
        pass