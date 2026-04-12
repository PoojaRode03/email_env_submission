# test_env.py
import asyncio
from client import EmailEnv

async def run_tests():
    env = EmailEnv()
    
    print("=== Resetting Environment ===")
    reset_response = await env.reset()
    print(reset_response)
    print("\n=== Running Tasks ===\n")

    test_emails = [
        {"message": "You won the lottery! Claim now!", "task": "spam"},
        {"message": "Hello, just checking in.", "task": "spam"},
        {"message": "Meeting at 10 AM tomorrow.", "task": "category"},
        {"message": "Lunch with friend.", "task": "category"},
        {"message": "Please draft a reply for this email.", "task": "reply"}
    ]

    for email in test_emails:
        response = await env.step(email)
        print(f"Task: {email['task']} | Message: {email['message']}")
        print(f"Response: {response}\n")

if __name__ == "__main__":
    asyncio.run(run_tests())