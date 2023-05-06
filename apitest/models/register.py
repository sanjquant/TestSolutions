from dataclasses import dataclass
from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Register:
    email: str
    password: str

    @staticmethod
    def from_dict(obj: Any) -> 'Register':
        assert isinstance(obj, dict)
        email = from_str(obj.get("email"))
        password = from_str(obj.get("password"))
        return Register(email, password)

    def to_dict(self) -> dict:
        result: dict = {}
        result["email"] = from_str(self.email)
        result["password"] = from_str(self.password)
        return result


def register_from_dict(s: Any) -> Register:
    return Register.from_dict(s)


def register_to_dict(x: Register) -> Any:
    return to_class(Register, x)
