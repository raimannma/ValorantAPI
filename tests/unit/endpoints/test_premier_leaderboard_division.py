from typing import Optional

import urllib.parse
from uuid import UUID

import pytest
import responses
from aioresponses import aioresponses
from hypothesis import given, settings
from hypothesis import strategies as st
from responses import matchers

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
    version=st.sampled_from(["v1"]),
    affinity=st.text(),
    conference=st.text(),
    division=st.text(),
)
@responses.activate
@pytest.mark.asyncio
async def test_get_premier_leaderboard_by_division(
    version: str, affinity: str, conference: str, division: str,
):
    print(f"Test get_premier_leaderboard_by_division with: {locals()}")

    encoded_affinity = urllib.parse.quote_plus(affinity).lower()
    encoded_conference = urllib.parse.quote_plus(conference).lower()
    encoded_division = urllib.parse.quote_plus(division).lower()

    url = f"{Config.BASE_URL}/valorant/{version}/premier/leaderboard/{encoded_affinity}/{encoded_conference}/{encoded_division}"

    responses.add(
        responses.GET,
        url,
        json=get_mock_response(f"premier_leaderboard_by_division_{version}.json"),
        status=200,
    )

    getattr(valo_api, f"get_premier_leaderboard_by_division_{version}")(affinity=affinity, conference=conference, division=division)
    assert len(responses.calls) == 1

    getattr(valo_api, "get_premier_leaderboard_by_division")(version=version, affinity=affinity, conference=conference, division=division)
    assert len(responses.calls) == 2


@given(
    version=st.sampled_from(["v1"]),
    affinity=st.text(),
    conference=st.text(),
    division=st.text(),
    error_response=st.sampled_from(get_error_responses("mmr_details")),
)
@responses.activate
@pytest.mark.asyncio
async def test_get_premier_leaderboard_by_division_error(
    version: str,
    affinity: str,
    conference: str,
    division: str,
    error_response: dict,
):
    print(f"Test test_get_premier_leaderboard_by_division_error with: {locals()}")

    encoded_affinity = urllib.parse.quote_plus(affinity).lower()
    encoded_conference = urllib.parse.quote_plus(conference).lower()
    encoded_division = urllib.parse.quote_plus(division).lower()

    url = f"{Config.BASE_URL}/valorant/{version}/premier/leaderboard/{encoded_affinity}/{encoded_conference}/{encoded_division}"

    responses.add(
        responses.GET,
        url,
        json=error_response,
        status=int(error_response["status"]) if "status" in error_response else 500,
    )

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, f"get_premier_leaderboard_by_division_{version}")(affinity=affinity, conference=conference, division=division)
        validate_exception(error_response, excinfo)
    assert len(responses.calls) == 1

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, "get_premier_leaderboard_by_division")(version=version, affinity=affinity, conference=conference, division=division)
        validate_exception(error_response, excinfo)
    assert len(responses.calls) == 2


if __name__ == "__main__":
    test_get_premier_leaderboard_by_division()
    test_get_premier_leaderboard_by_division_error()
