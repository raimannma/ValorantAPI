from typing import Optional

import urllib.parse
from uuid import UUID

import pytest
import responses
from aioresponses import aioresponses
from hypothesis import given
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


@given(
    version=st.sampled_from(["v1"]),
)
@responses.activate
@pytest.mark.asyncio
async def test_get_premier_seasons(
    version: str,
):
    print(f"Test get_premier_seasons with: {locals()}")

    url = f"{Config.BASE_URL}/valorant/{version}/premier/seasons"

    responses.add(
        responses.GET,
        url,
        json=get_mock_response(f"premier_seasons_{version}.json"),
        status=200,
    )

    getattr(valo_api, f"get_premier_seasons_{version}")()
    assert len(responses.calls) == 1

    getattr(valo_api, "get_premier_seasons")(version=version)
    assert len(responses.calls) == 2


@given(
    version=st.sampled_from(["v1"]),
    error_response=st.sampled_from(get_error_responses("mmr_details")),
)
@responses.activate
@pytest.mark.asyncio
async def test_get_premier_seasons_error(
    version: str,
    error_response: dict,
):
    print(f"Test test_get_premier_seasons_error with: {locals()}")

    url = f"{Config.BASE_URL}/valorant/{version}/premier/seasons"

    responses.add(
        responses.GET,
        url,
        json=error_response,
        status=int(error_response["status"]) if "status" in error_response else 500,
    )

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, f"get_premier_seasons_{version}")()
        validate_exception(error_response, excinfo)
    assert len(responses.calls) == 1

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, "get_premier_seasons")(version=version)
        validate_exception(error_response, excinfo)
    assert len(responses.calls) == 2


if __name__ == "__main__":
    test_get_premier_seasons()
    test_get_premier_seasons_error()
