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
    region=st.sampled_from(Config.ALL_REGIONS),
    name=st.text(),
    tag=st.text(),
    mode=st.one_of(st.none(), st.sampled_from(["competitive", "unrated"])),
    map=st.one_of(st.none(), st.sampled_from(["ascent", "bind", "haven", "split"])),
    page=st.one_of(st.none(), st.integers(min_value=1, max_value=100)),
    size=st.one_of(st.none(), st.integers(min_value=1, max_value=100)),
)
@responses.activate
@pytest.mark.asyncio
async def test_get_lifetime_matches_by_name(
    version: str,
    region: str,
    name: str,
    tag: str,
    mode: Optional[str],
    map: Optional[str],
    page: Optional[int],
    size: Optional[int],
):
    print(f"Test get_lifetime_matches_by_name with: {locals()}")

    encoded_name = urllib.parse.quote_plus(name).lower()
    encoded_tag = urllib.parse.quote_plus(tag).lower()

    url = f"{Config.BASE_URL}/valorant/{version}/lifetime/matches/{region}/{encoded_name}/{encoded_tag}"
    params = {}
    if mode is not None:
        params["mode"] = mode
    if map is not None:
        params["map"] = map
    if page is not None:
        params["page"] = page
        if size is None:
            params["size"] = 20
            size = 20
    if size is not None:
        params["size"] = size
        if page is None:
            params["page"] = 1
            page = 1

    responses.add(
        responses.GET,
        url,
        json=get_mock_response(f"lifetime_matches_by_name_{version}.json"),
        match={matchers.query_param_matcher(params)},
        status=200,
    )

    getattr(valo_api, f"get_lifetime_matches_by_name_{version}")(
        region=region, name=name, tag=tag, mode=mode, map=map, page=page, size=size
    )
    assert len(responses.calls) == 1

    getattr(valo_api, "get_lifetime_matches_by_name")(
        version=version,
        region=region,
        name=name,
        tag=tag,
        mode=mode,
        map=map,
        page=page,
        size=size,
    )
    assert len(responses.calls) == 2


@given(
    version=st.sampled_from(["v1"]),
    region=st.sampled_from(Config.ALL_REGIONS),
    name=st.text(),
    tag=st.text(),
    mode=st.one_of(st.none(), st.sampled_from(["competitive", "unrated"])),
    map=st.one_of(st.none(), st.sampled_from(["ascent", "bind", "haven", "split"])),
    page=st.one_of(st.none(), st.integers(min_value=1, max_value=100)),
    size=st.one_of(st.none(), st.integers(min_value=1, max_value=100)),
    error_response=st.sampled_from(get_error_responses("lifetime_matches")),
)
@responses.activate
@pytest.mark.asyncio
async def test_get_lifetime_matches_by_name_error(
    version: str,
    region: str,
    name: str,
    tag: str,
    mode: Optional[str],
    map: Optional[str],
    page: Optional[int],
    size: Optional[int],
    error_response: dict,
):
    print(f"Test get_lifetime_matches_by_name_error with: {locals()}")

    encoded_name = urllib.parse.quote_plus(name).lower()
    encoded_tag = urllib.parse.quote_plus(tag).lower()

    url = f"{Config.BASE_URL}/valorant/{version}/lifetime/matches/{region}/{encoded_name}/{encoded_tag}"
    params = {}
    if mode is not None:
        params["mode"] = mode
    if map is not None:
        params["map"] = map
    if page is not None:
        params["page"] = page
        if size is None:
            params["size"] = 20
            size = 20
    if size is not None:
        params["size"] = size
        if page is None:
            params["page"] = 1
            page = 1

    responses.add(
        responses.GET,
        url,
        match=[matchers.query_param_matcher(params)],
        json=error_response,
        status=int(error_response["status"]) if "status" in error_response else 500,
    )

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, f"get_lifetime_matches_by_name_{version}")(
            region=region, name=name, tag=tag, mode=mode, map=map, page=page, size=size
        )
        validate_exception(error_response, excinfo)
    assert len(responses.calls) == 1

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, "get_lifetime_matches_by_name")(
            version=version,
            region=region,
            name=name,
            tag=tag,
            mode=mode,
            map=map,
            page=page,
            size=size,
        )
        validate_exception(error_response, excinfo)
    assert len(responses.calls) == 2


@given(
    version=st.sampled_from(["v1"]),
    region=st.sampled_from(Config.ALL_REGIONS),
    puuid=st.uuids(),
    mode=st.one_of(st.none(), st.sampled_from(["competitive", "unrated"])),
    map=st.one_of(st.none(), st.sampled_from(["ascent", "bind", "haven", "split"])),
    page=st.one_of(st.none(), st.integers(min_value=1, max_value=100)),
    size=st.one_of(st.none(), st.integers(min_value=1, max_value=100)),
)
@responses.activate
@pytest.mark.asyncio
async def test_get_lifetime_matches_by_puuid(
    version: str,
    region: str,
    puuid: UUID,
    mode: Optional[str],
    map: Optional[str],
    page: Optional[int],
    size: Optional[int],
):
    print(f"Test get_lifetime_matches_by_puuid with: {locals()}")

    puuid = str(puuid).lower()

    url = f"{Config.BASE_URL}/valorant/{version}/by-puuid/lifetime/matches/{region}/{puuid}"
    params = {}
    if mode is not None:
        params["mode"] = mode
    if map is not None:
        params["map"] = map
    if page is not None:
        params["page"] = page
        if size is None:
            params["size"] = 20
            size = 20
    if size is not None:
        params["size"] = size
        if page is None:
            params["page"] = 1
            page = 1

    responses.add(
        responses.GET,
        url,
        json=get_mock_response(f"lifetime_matches_by_puuid_{version}.json"),
        match={matchers.query_param_matcher(params)},
        status=200,
    )

    getattr(valo_api, f"get_lifetime_matches_by_puuid_{version}")(
        region=region, puuid=puuid, mode=mode, map=map, page=page, size=size
    )
    assert len(responses.calls) == 1

    getattr(valo_api, "get_lifetime_matches_by_puuid")(
        version=version,
        region=region,
        puuid=puuid,
        mode=mode,
        map=map,
        page=page,
        size=size,
    )
    assert len(responses.calls) == 2


@given(
    version=st.sampled_from(["v1"]),
    region=st.sampled_from(Config.ALL_REGIONS),
    puuid=st.uuids(),
    mode=st.one_of(st.none(), st.sampled_from(["competitive", "unrated"])),
    map=st.one_of(st.none(), st.sampled_from(["ascent", "bind", "haven", "split"])),
    page=st.one_of(st.none(), st.integers(min_value=1, max_value=100)),
    size=st.one_of(st.none(), st.integers(min_value=1, max_value=100)),
    error_response=st.sampled_from(get_error_responses("mmr_details")),
)
@responses.activate
@pytest.mark.asyncio
async def test_get_lifetime_matches_by_puuid_error(
    version: str,
    region: str,
    puuid: UUID,
    mode: Optional[str],
    map: Optional[str],
    page: Optional[int],
    size: Optional[int],
    error_response: dict,
):
    print(f"Test get_lifetime_matches_by_puuid_error with: {locals()}")

    url = f"{Config.BASE_URL}/valorant/{version}/by-puuid/lifetime/matches/{region}/{puuid}"
    params = {}
    if mode is not None:
        params["mode"] = mode
    if map is not None:
        params["map"] = map
    if page is not None:
        params["page"] = page
        if size is None:
            params["size"] = 20
            size = 20
    if size is not None:
        params["size"] = size
        if page is None:
            params["page"] = 1
            page = 1

    responses.add(
        responses.GET,
        url,
        match=[matchers.query_param_matcher(params)],
        json=error_response,
        status=int(error_response["status"]) if "status" in error_response else 500,
    )

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, f"get_lifetime_matches_by_puuid_{version}")(
            region=region, puuid=puuid, mode=mode, map=map, page=page, size=size
        )
        validate_exception(error_response, excinfo)
    assert len(responses.calls) == 1

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, "get_lifetime_matches_by_puuid")(
            version=version,
            region=region,
            puuid=puuid,
            mode=mode,
            map=map,
            page=page,
            size=size,
        )
        validate_exception(error_response, excinfo)
    assert len(responses.calls) == 2


if __name__ == "__main__":
    test_get_lifetime_matches_by_name()
    test_get_lifetime_matches_by_name_error()
    test_get_lifetime_matches_by_puuid()
    test_get_lifetime_matches_by_puuid_error()
