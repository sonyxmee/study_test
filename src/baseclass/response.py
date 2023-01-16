from jsonschema import validate
from src.enum.enums import ErrorMessage


class Response:
    def __init__(self, response):
        self.response = response
        self.response_code = response.status_code
        self.response_json = response.json()

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_code in status_code, ErrorMessage.WRONG_STATUS_CODE.value
        else:
            assert self.response_code == 200, ErrorMessage.WRONG_STATUS_CODE.value

        return self

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                validate(item, schema)
        else:
            validate(self.response_json, schema)
