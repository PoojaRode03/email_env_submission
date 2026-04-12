import asyncio
from client import EmailEnv

async def main():
    env = EmailEnv()

    result = await env.reset()
    print("Initial:", result)

    action = {
        "action": {
        "message": "You won a lottery!!!",
        "task": "spam"
    }
    }

    result = await env.step(action)
    print("Result:", result)

if __name__ == "__main__":
    asyncio.run(main())