from pathlib import Path
import json
import requests
from enum import Enum
import jsonpath as jp
# from jsonpath_rw import jsonpath, parse
from jsonpath_ng.ext import parse


class ENDPOINTS(Enum):
    BASE_URL = "https://reqres.in/"
    REGISTER_ENDPOINT = "api/register"
    LOGIN_ENDPOINT = "api/login"
    RESOURSES_ENDPOINT = "api/unknown"


class HEADERS(Enum):
    CONTENT_TYPE = "application/json;charset=utf-8"


class FILEDIRECTORY(Enum):
    FEATURE_FILE_DIR = "featureFiles"
    FILE_DIR_NAME = "files"


class Utils:

    def __init__(self, featurefileName):
        self.BASE_DIR: str = None
        self.featurefileName: str = featurefileName
        self.featurefiledir: str = FILEDIRECTORY.FEATURE_FILE_DIR.value
        self.file_dir = FILEDIRECTORY.FILE_DIR_NAME.value
        self.base_url: str = ENDPOINTS.BASE_URL.value
        self.contentType: str = HEADERS.CONTENT_TYPE.value
        self.registerEndPoint: str = ENDPOINTS.REGISTER_ENDPOINT.value
        self.login_endpoint: str = ENDPOINTS.LOGIN_ENDPOINT.value
        self.resources_endpoint: str = ENDPOINTS.RESOURSES_ENDPOINT.value
        self.get_parent()

    def get_parent(self):
        self.BASE_DIR = Path(__file__).resolve().parent
        print(self.BASE_DIR)

    def get_feature_file_dir(self):
        return self.BASE_DIR.joinpath(self.featurefiledir).joinpath(self.featurefileName)

    def get_test_data_file_path(self, filename):
        return self.BASE_DIR.joinpath(self.file_dir).joinpath(filename)

    def get_test_data(self, filename):
        with open(self.get_test_data_file_path(filename), 'r') as f:
            data = json.load(f)
        return data

    def send_post_request(self, api_endpoints, request_bodies, request_headers):
        response = requests.post(url=api_endpoints, json=request_bodies, headers=request_headers)
        return response

    def send_get_request(self, api_endpoints, request_headers):
        response = requests.get(url=api_endpoints, headers=request_headers)
        return response

    def get_json_value(self, jsonExpression, data):
        # json_response = json.dumps(data)
        json_data = json.loads(data)
        # value = jp.jsonpath(data, jsonExpression)
        js_exp = parse(jsonExpression)
        match_value = js_exp.find(json_data)
        return match_value
