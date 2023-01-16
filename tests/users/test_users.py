import requests

from configurations import URL
from src.baseclass.response import Response
from src.pydantic_schemas.user import User


def test_request_post(get_users):
    response = Response(get_users)
    response.assert_status_code(200).validate(User)
