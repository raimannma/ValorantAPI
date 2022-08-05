import urllib.parse

import pytest
import responses
from hypothesis import given, settings
from hypothesis import strategies as st

import valo_api
from tests.unit.endpoints.utils import (
    get_error_responses,
    get_mock_response,
    validate_exception,
)
from valo_api.config import Config
from valo_api.exceptions.valo_api_exception import ValoAPIException


@settings(deadline=None)
@given(
    version=st.sampled_from(["v1", "v2"]), region=st.sampled_from(Config.ALL_REGIONS)
)
@responses.activate
def test_get_leaderboard(version: str, region: str):
    print(f"Test get_leaderboard with: {locals()}")

    encoded_region = urllib.parse.quote_plus(region).lower()

    url = f"{Config.BASE_URL}/valorant/{version}/leaderboard/{encoded_region}"

    responses.add(
        responses.GET,
        url,
        json=get_mock_response(f"leaderboard_{version}.json"),
        status=200,
    )

    getattr(valo_api, f"get_leaderboard_{version}")(region=region)
    assert len(responses.calls) == 1

    getattr(valo_api, "get_leaderboard")(version=version, region=region)
    assert len(responses.calls) == 2


@given(
    version=st.sampled_from(["v1", "v2"]),
    region=st.sampled_from(Config.ALL_REGIONS),
    error_response=st.sampled_from(get_error_responses("leaderboard")),
)
@responses.activate
def test_get_leaderboard_error(version: str, region: str, error_response: dict):
    print(f"Test test_get_leaderboard_error with: {locals()}")

    encoded_region = urllib.parse.quote_plus(region).lower()

    url = f"{Config.BASE_URL}/valorant/{version}/leaderboard/{encoded_region}"

    responses.add(
        responses.GET,
        url,
        json=error_response,
        status=int(error_response["status"]) if "status" in error_response else 500,
    )

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, f"get_leaderboard_{version}")(region=region)
    assert len(responses.calls) == 1
    validate_exception(error_response, excinfo)

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, "get_leaderboard")(version=version, region=region)
    assert len(responses.calls) == 2
    validate_exception(error_response, excinfo)


if __name__ == "__main__":
    test_get_leaderboard()
    test_get_leaderboard_error()
