# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

# client.py

# Try importing the real OpenEnv first
#email_env_hf/client.py
import requests

class EmailEnv:
    def __init__(self):
        self.base_url = "http://127.0.0.1:8000"
        self.step_count = 0

    async def reset(self):
        self.step_count = 0

        response = requests.post(
            f"{self.base_url}/reset",
            json={
                "episode_id": "episode-001",
                "seed": 42
            }
        )
        return response.json()

    async def step(self, action):
        self.step_count += 1

        response = requests.post(
            f"{self.base_url}/step",
            json=action   # 🔥 FIX HERE
        )

        data = response.json()


        return data