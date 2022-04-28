import json
import os


def get_mock_response(filename: str):
    path = os.path.join(os.path.dirname(__file__), "mock_responses", filename)
    with open(path) as f:
        return json.load(f)
