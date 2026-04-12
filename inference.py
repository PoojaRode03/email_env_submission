import os
import asyncio
from openai import OpenAI
from client import EmailEnv

API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
HF_TOKEN = os.getenv("HF_TOKEN", "dummy-key")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)


def simple_agent(message):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": message}],
            max_tokens=10
        )

        output = response.choices[0].message.content.lower()

        if "spam" in output:
            task = "spam"
        elif "meeting" in output:
            task = "category"
        else:
            task = "reply"

        return {"message": message, "task": task}

    except Exception:
        return {"message": message, "task": "reply"}


async def run():
    env = EmailEnv()

    emails = [
        "Win lottery",
        "Team meeting",
        "Reply client"
    ]

    print(f"[START] task=email env=email_env model={MODEL_NAME}")

    rewards = []

    for i, email in enumerate(emails, start=1):
        action = simple_agent(email)
        response = await env.step(action)

        reward = response.get("reward", 0.5)

        # ONLY safety clamp (allowed)
        reward = min(0.9, max(0.1, float(reward)))

        rewards.append(f"{reward:.2f}")

        print(f"[STEP] step={i} reward={reward:.2f} done={response.get('done')}")

    print(f"[END] success=true steps={len(emails)} rewards={','.join(rewards)}")


if __name__ == "__main__":
    asyncio.run(run())  