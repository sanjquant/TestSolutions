from dataclasses import dataclass
from typing import Any, List, TypeVar, Callable, Type, cast

from enum import Enum
import requests
from requests import Response


def combine_endpoint(base_url: str, endpoint: str) -> str:
    return f"{base_url}{endpoint}"


class ENDPOINTS(Enum):
    BASE_URL = "https://reqres.in/"
    REGISTER_ENDPOINT = "api/register"
    LOGIN_ENDPOINT = "api/login"
    RESOURSES_ENDPOINT = "api/unknown"


@dataclass
class Helper(Enum):
    base_url: str = ENDPOINTS.BASE_URL.value
    url: str = None

    def set_url(self, endpoint: str):
        url: str = combine_endpoint(self.base_url, endpoint)
        return url

    def send_get_request(self, api_endpoints, request_headers):
        response = requests.get(url=self.set_url(api_endpoints), headers=request_headers)
        return response

    def send_post_request(self, api_endpoints: str, request_bodies: Any, request_headers: Any):
        response: Response = requests.post(url=self.set_url(api_endpoints), json=request_bodies,
                                           headers=request_headers)
        return response

    def get_content(self, response: Response) -> Any:
        response_data = response.text
        return response_data

    

