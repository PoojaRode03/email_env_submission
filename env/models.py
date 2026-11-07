from openenv.core.env_server import Action, Observation


class EmailAction(Action):
    message: str
    task: str


class EmailObservation(Observation):
    observation: str
    reward: float
    done: bool