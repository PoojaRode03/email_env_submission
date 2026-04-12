#email_env_hf/baseline.py
import asyncio
from client import EmailEnv

async def run():
    env = EmailEnv()

    await env.reset()

    tasks = [
        {"message": "Win lottery now", "task": "spam"},
        {"message": "Team meeting at 5", "task": "category"},
        {"message": "Can we meet tomorrow?", "task": "reply"}
    ]

    total_score = 0

    for t in tasks:
        result = await env.step({
            "message": t["message"],
            "task": t["task"]
        })

        print("Step result:", result)

        reward = result.get("reward", 0)
        total_score += reward

    print("Final Score:", total_score / len(tasks))

asyncio.run(run())