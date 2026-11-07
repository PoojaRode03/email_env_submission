from openenv.core.env_server import create_app

from env.models import EmailAction, EmailObservation
from server.email_env_environment import EmailEnvironment
from env.tasks import get_tasks


# Register the three available tasks
TASKS = get_tasks()

print("🔥 TASKS LOADED IN SERVER:", len(TASKS))
print([task["id"] for task in TASKS])


# Create the OpenEnv FastAPI application
app = create_app(
    env=EmailEnvironment,
    action_cls=EmailAction,
    observation_cls=EmailObservation,
    env_name="email_env",
)