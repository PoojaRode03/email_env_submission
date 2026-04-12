# /email_env/email_env/env/models.py
from pydantic import BaseModel

class EmailAction(BaseModel):
    email_id: int
    action_type: str
    value: str = None


class EmailObservation(BaseModel):
    observation: str
    reward: float
    done: bool