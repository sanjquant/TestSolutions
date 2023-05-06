import json
from dataclasses import dataclass


@dataclass
class Login:
    email: str
    password: str


def as_payload(message):
    # Deserialization
    decoded_payload = Login(**json.loads(message))
    return decoded_payload


def login_obj(message):
    obj = json.loads(message, object_hook=as_payload)
    return obj
