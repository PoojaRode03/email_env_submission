# mock_openenv.py

# -------------------------
# Mock Environment
# -------------------------
class Environment:
    def reset(self):
        print("[Mock] Environment reset")
        return "mock_state"

    def step(self, action):
        print(f"[Mock] Step called with action: {action}")
        return "mock_state", 0, False, {}

    @property
    def state(self):
        return "mock_state"

    def render(self):
        print("[Mock] Render called")


# -------------------------
# Mock EnvClient
# -------------------------
class EnvClient:
    # Allow subscription syntax EnvClient[...] without error
    def __class_getitem__(cls, item):
        return cls

    def __init__(self, *args, **kwargs):
        print("[Mock] EnvClient created")


# -------------------------
# Mock Types
# -------------------------
class State:
    pass

class StepResult:
    pass

class Action:
    pass

class Observation:
    pass