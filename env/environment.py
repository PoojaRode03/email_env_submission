#env/environment.py
class EmailEnv:

    def reset(self):
        self.emails = [
            {"id": 0, "type": "spam"},
            {"id": 1, "type": "important"},
            {"id": 2, "type": "spam"}
        ]
        self.step_count = 0
        return self.state()

    def state(self):
        return self.emails

    def step(self, action):
        self.step_count += 1

        email = self.emails[action.email_id]

        reward = 0.5
        done = False

        if action.action_type == "classify":
            if action.value == email["type"]:
                reward = 0.95
            else:
                reward = 0.05

        elif action.action_type == "prioritize":
            reward = 0.7

        elif action.action_type == "reply":
            reward = 0.75

        # terminate after fixed steps
        if self.step_count >= len(self.emails):
            done = True

        return self.state(), reward, done, {}