import urllib.parse
from uuid import UUID

import pytest
import responses
from hypothesis import given
from hypothesis import strategies as st

import valo_api
from tests.unit.endpoints.utils import (
    get_error_responses,
    get_mock_response,
    validate_exception,
)
from valo_api.config import Config
from valo_api.exceptions.valo_api_exception import ValoAPIException


@given(
    version=st.sampled_from(["v2"]),
    match_id=st.uuids(),
)
@responses.activate
def test_get_match_details(version: str, match_id: UUID):
    print(f"Test get_match_details with: {locals()}")

    match_id = str(match_id)
    encoded_match_id = urllib.parse.quote_plus(match_id).lower()

    url = f"{Config.BASE_URL}/valorant/{version}/match/{encoded_match_id}"

    responses.add(
        responses.GET,
        url,
        json=get_mock_response(f"match_details_{version}.json"),
        status=200,
    )

    getattr(valo_api, f"get_match_details_{version}")(matchId=match_id)
    assert len(responses.calls) == 1

    getattr(valo_api, "get_match_details")(version=version, matchId=match_id)
    assert len(responses.calls) == 2


@given(
    version=st.sampled_from(["v2"]),
    match_id=st.uuids(),
    error_response=st.sampled_from(get_error_responses("match_details")),
)
@responses.activate
def test_get_match_details_error(version: str, match_id: UUID, error_response: dict):
    print(f"Test get_match_details with: {locals()}")

    match_id = str(match_id)
    encoded_match_id = urllib.parse.quote_plus(match_id).lower()

    url = f"{Config.BASE_URL}/valorant/{version}/match/{encoded_match_id}"

    responses.add(
        responses.GET,
        url,
        json=error_response,
        status=int(error_response["status"]) if "status" in error_response else 500,
    )

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, f"get_match_details_{version}")(matchId=match_id)
    assert len(responses.calls) == 1
    validate_exception(error_response, excinfo)

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, "get_match_details")(version=version, matchId=match_id)
    assert len(responses.calls) == 2
    validate_exception(error_response, excinfo)


if __name__ == "__main__":
    test_get_match_details()
    test_get_match_details_error()
