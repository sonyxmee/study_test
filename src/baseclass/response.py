from jsonschema import validate
from src.enum.global_enums import ErrorMessage


class Response:
    def __init__(self, response):
        self.response = response
        self.response_code = response.status_code
        self.response_json = response.json().get('data')

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_code in status_code, ErrorMessage.WRONG_STATUS_CODE.value  # self
        else:
            assert self.response_code == status_code, ErrorMessage.WRONG_STATUS_CODE.value  # self

        return self

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.parse_obj(item)
                # validate(item, schema)
        else:
            schema.parse_obj(self.response_json)
            # validate(self.response_json, schema)

    def __str__(self):
        return f"Requested url: {self.response.url}\n \
               Response status code: {self.response_code}\n \
               Response body: {self.response_json}"
