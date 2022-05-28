import json
import os

from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.error_response import ErrorResponse


def get_mock_response(filename: str):
    path = os.path.join(os.path.dirname(__file__), "mock_responses", filename)
    with open(path) as f:
        return json.load(f)


def get_error_responses(endpoint: str):
    path = os.path.join(
        os.path.dirname(__file__), "error_responses", f"{endpoint}.json"
    )
    with open(path) as f:
        return json.load(f)


def validate_exception(error_response, excinfo):
    assert isinstance(excinfo.value.args[0], ErrorResponse)
    assert isinstance(excinfo.value, ValoAPIException)
    if "status" in error_response:
        assert excinfo.value.status == int(error_response["status"])
    if "message" in error_response:
        assert excinfo.value.message == error_response["message"]
    if "errors" in error_response:
        assert excinfo.value.error == error_response["error"]
