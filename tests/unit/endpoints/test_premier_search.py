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
    name=st.one_of(st.none(), st.text(min_size=1)),
    tag=st.one_of(st.none(), st.text(min_size=1)),
    division=st.one_of(st.none(), st.integers()),
    conference=st.one_of(st.none(), st.text(min_size=1)),
)
@responses.activate
@pytest.mark.asyncio
async def test_get_premier_search(
    version: str,
    name: Optional[str],
    tag: Optional[str],
    division: Optional[int],
    conference: Optional[str],
):
    print(f"Test get_premier_search with: {locals()}")

    url = f"{Config.BASE_URL}/valorant/{version}/premier/search"
    params = {
        "name": name,
        "tag": tag,
        "division": division,
        "conference": conference,
    }

    params = {k: str(v).lower() for k, v in params.items() if v is not None}

    responses.add(
        responses.GET,
        url,
        json=get_mock_response(f"premier_search_{version}.json"),
        match=[matchers.query_param_matcher(params)],
        status=200,
    )

    getattr(valo_api, f"get_premier_search_{version}")(name=name, tag=tag, division=division, conference=conference)
    assert len(responses.calls) == 1

    getattr(valo_api, "get_premier_search")(version=version, name=name, tag=tag, division=division, conference=conference)
    assert len(responses.calls) == 2


@given(
    version=st.sampled_from(["v1"]),
    name=st.one_of(st.none(), st.text(min_size=1)),
    tag=st.one_of(st.none(), st.text(min_size=1)),
    division=st.one_of(st.none(), st.integers()),
    conference=st.one_of(st.none(), st.text(min_size=1)),
    error_response=st.sampled_from(get_error_responses("mmr_details")),
)
@responses.activate
@pytest.mark.asyncio
async def test_get_premier_search_error(
    version: str,
    name: Optional[str],
    tag: Optional[str],
    division: Optional[int],
    conference: Optional[str],
    error_response: dict,
):
    print(f"Test test_get_premier_search_error with: {locals()}")

    url = f"{Config.BASE_URL}/valorant/{version}/premier/search"
    params = {
        "name": name,
        "tag": tag,
        "division": division,
        "conference": conference,
    }

    params = {k: str(v).lower() for k, v in params.items() if v is not None}

    responses.add(
        responses.GET,
        url,
        json=error_response,
        match=[matchers.query_param_matcher(params)],
        status=int(error_response["status"]) if "status" in error_response else 500,
    )

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, f"get_premier_search_{version}")(name=name, tag=tag, division=division, conference=conference)
        validate_exception(error_response, excinfo)
    assert len(responses.calls) == 1

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, "get_premier_search")(version=version, name=name, tag=tag, division=division, conference=conference)
        validate_exception(error_response, excinfo)
    assert len(responses.calls) == 2


if __name__ == "__main__":
    test_get_premier_search()
    test_get_premier_search_error()
