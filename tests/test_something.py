import requests

from configurations import URL
from src.baseclass.response import Response
from src.schemas.schemas import POST_SCHEMA


def test_request_post():
    r = requests.get(url=URL)
    response = Response(r)
    response.assert_status_code(200).validate(POST_SCHEMA)
