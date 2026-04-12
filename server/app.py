#server/app.py
from fastapi import FastAPI
from env.tasks import get_tasks
from pydantic import BaseModel
import uvicorn
from env import graders

def resolve_grader(name):
    return getattr(graders, name)
app = FastAPI()

# ---------------- TASK REGISTRY (IMPORTANT) ----------------
TASKS = get_tasks()

for t in TASKS:
    if isinstance(t["grader"], str):
        t["grader"] = resolve_grader(t["grader"])

app.state.tasks = TASKS

print("🔥 TASKS LOADED IN SERVER:", len(TASKS))
print([t["id"] for t in TASKS])


# ---------------- Models ----------------
class StepRequest(BaseModel):
    message: str
    task: str


# ---------------- Environment ----------------
class EmailEnvironment:
    def __init__(self):
        self.step_count = 0

    def reset(self):
        self.step_count = 0
        return {"observation": "reset done", "reward": 0.3, "done": False}

    def step(self, message, task):
        self.step_count += 1

        message = message.lower()
        task = task.lower()

        if task == "spam":
            if "win" in message or "lottery" in message:
                return {"observation": "Spam detected", "reward": 0.83, "done": True}
            return {"observation": "Not spam", "reward": 0.27, "done": True}

        elif task == "category":
            if "meeting" in message:
                return {"observation": "Work email", "reward": 0.74, "done": True}
            return {"observation": "Other email", "reward": 0.41, "done": True}

        elif task == "reply":
            return {"observation": "Reply generated", "reward": 0.68, "done": True}

        return {"observation": "Invalid task", "reward": 0.19, "done": True}


env = EmailEnvironment()


# ---------------- Routes ----------------
@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(req: StepRequest):
    return env.step(req.message, req.task)

@app.get("/state")
def state():
    return env.state()

@app.get("/")
def home():
    return {"status": "Email Env running"}


# ---------------- Main ----------------
def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()