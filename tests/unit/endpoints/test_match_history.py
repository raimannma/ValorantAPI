from typing import Optional

import urllib.parse
from uuid import UUID

import pytest
import responses
from aioresponses import aioresponses
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
    version=st.sampled_from(["v3"]),
    region=st.sampled_from(Config.ALL_REGIONS),
    name=st.text(),
    tag=st.text(),
    size=st.one_of(st.none(), st.integers(min_value=1, max_value=5)),
)
@responses.activate
@pytest.mark.asyncio
async def test_get_match_history_by_name(
    version: str, region: str, name: str, tag: str, size: Optional[int]
):
    print(f"Test get_match_history_by_name with: {locals()}")

    encoded_name = urllib.parse.quote_plus(name).lower()
    encoded_tag = urllib.parse.quote_plus(tag).lower()

    url = f"{Config.BASE_URL}/valorant/{version}/matches/{region}/{encoded_name}/{encoded_tag}"

    responses.add(
        responses.GET,
        url,
        json=get_mock_response(f"match_history_by_name_{version}.json"),
        status=200,
    )

    getattr(valo_api, f"get_match_history_by_name_{version}")(
        region=region, name=name, tag=tag, size=size
    )
    assert len(responses.calls) == 1

    getattr(valo_api, "get_match_history_by_name")(
        version=version, region=region, name=name, tag=tag, size=size
    )
    assert len(responses.calls) == 2

    with aioresponses() as m:
        m.get(url, payload=get_mock_response(f"match_history_by_name_{version}.json"))
        m.get(
            f"{url}?size={size}",
            payload=get_mock_response(f"match_history_by_name_{version}.json"),
        )
        await getattr(valo_api, f"get_match_history_by_name_{version}_async")(
            region=region, name=name, tag=tag, size=size
        )
        m.assert_called_once()

    with aioresponses() as m:
        m.get(url, payload=get_mock_response(f"match_history_by_name_{version}.json"))
        m.get(
            f"{url}?size={size}",
            payload=get_mock_response(f"match_history_by_name_{version}.json"),
        )
        await getattr(valo_api, "get_match_history_by_name_async")(
            version=version, region=region, name=name, tag=tag, size=size
        )
        m.assert_called_once()


@given(
    version=st.sampled_from(["v3"]),
    region=st.sampled_from(Config.ALL_REGIONS),
    name=st.text(),
    tag=st.text(),
    size=st.one_of(st.none(), st.integers(min_value=1, max_value=5)),
    error_response=st.sampled_from(get_error_responses("match_history")),
)
@responses.activate
@pytest.mark.asyncio
async def test_get_match_history_by_name_error(
    version: str,
    region: str,
    name: str,
    tag: str,
    size: Optional[int],
    error_response: dict,
):
    print(f"Test test_get_match_history_by_name_error with: {locals()}")

    encoded_name = urllib.parse.quote_plus(name).lower()
    encoded_tag = urllib.parse.quote_plus(tag).lower()

    url = f"{Config.BASE_URL}/valorant/{version}/matches/{region}/{encoded_name}/{encoded_tag}"

    responses.add(
        responses.GET,
        url,
        json=error_response,
        status=int(error_response["status"]) if "status" in error_response else 500,
    )

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, f"get_match_history_by_name_{version}")(
            region=region, name=name, tag=tag, size=size
        )
        validate_exception(error_response, excinfo)
    assert len(responses.calls) == 1

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, "get_match_history_by_name")(
            version=version, region=region, name=name, tag=tag, size=size
        )
        validate_exception(error_response, excinfo)
    assert len(responses.calls) == 2

    with aioresponses() as m:
        m.get(url, payload=error_response, exception=ValoAPIException(error_response))
        m.get(
            f"{url}?size={size}",
            payload=error_response,
            exception=ValoAPIException(error_response),
        )
        with pytest.raises(ValoAPIException) as excinfo:
            await getattr(valo_api, f"get_match_history_by_name_{version}_async")(
                region=region, name=name, tag=tag, size=size
            )
            validate_exception(error_response, excinfo)
        m.assert_called_once()

    with aioresponses() as m:
        m.get(url, payload=error_response, exception=ValoAPIException(error_response))
        m.get(
            f"{url}?size={size}",
            payload=error_response,
            exception=ValoAPIException(error_response),
        )
        with pytest.raises(ValoAPIException) as excinfo:
            await getattr(valo_api, "get_match_history_by_name_async")(
                version=version, region=region, name=name, tag=tag, size=size
            )
            validate_exception(error_response, excinfo)
        m.assert_called_once()


@settings(deadline=None)
@given(
    version=st.sampled_from(["v3"]),
    region=st.sampled_from(Config.ALL_REGIONS),
    puuid=st.uuids(),
    size=st.one_of(st.none(), st.integers(min_value=1, max_value=5)),
)
@responses.activate
@pytest.mark.asyncio
async def test_get_match_history_by_puuid(
    version: str, region: str, puuid: UUID, size: Optional[int]
):
    print(f"Test get_match_history_by_puuid with: {locals()}")

    puuid = str(puuid).lower()

    url = f"{Config.BASE_URL}/valorant/{version}/by-puuid/matches/{region}/{puuid}"

    responses.add(
        responses.GET,
        url,
        json=get_mock_response(f"match_history_by_puuid_{version}.json"),
        status=200,
    )

    getattr(valo_api, f"get_match_history_by_puuid_{version}")(
        region=region, puuid=puuid, size=size
    )
    assert len(responses.calls) == 1

    getattr(valo_api, "get_match_history_by_puuid")(
        version=version, region=region, puuid=puuid, size=size
    )
    assert len(responses.calls) == 2

    with aioresponses() as m:
        m.get(url, payload=get_mock_response(f"match_history_by_puuid_{version}.json"))
        m.get(
            f"{url}?size={size}",
            payload=get_mock_response(f"match_history_by_puuid_{version}.json"),
        )
        await getattr(valo_api, f"get_match_history_by_puuid_{version}_async")(
            region=region, puuid=puuid, size=size
        )
        m.assert_called_once()

    with aioresponses() as m:
        m.get(url, payload=get_mock_response(f"match_history_by_puuid_{version}.json"))
        m.get(
            f"{url}?size={size}",
            payload=get_mock_response(f"match_history_by_puuid_{version}.json"),
        )
        await getattr(valo_api, "get_match_history_by_puuid_async")(
            version=version, region=region, puuid=puuid, size=size
        )
        m.assert_called_once()


@given(
    version=st.sampled_from(["v3"]),
    region=st.sampled_from(Config.ALL_REGIONS),
    puuid=st.uuids(),
    size=st.one_of(st.none(), st.integers(min_value=1, max_value=5)),
    error_response=st.sampled_from(get_error_responses("match_history")),
)
@responses.activate
@pytest.mark.asyncio
async def test_get_match_history_by_puuid_error(
    version: str, region: str, puuid: UUID, size: Optional[int], error_response: dict
):
    print(f"Test get_match_history_by_puuid_error with: {locals()}")

    puuid = str(puuid).lower()

    url = f"{Config.BASE_URL}/valorant/{version}/by-puuid/matches/{region}/{puuid}"

    responses.add(
        responses.GET,
        url,
        json=error_response,
        status=int(error_response["status"]) if "status" in error_response else 500,
    )

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, f"get_match_history_by_puuid_{version}")(
            region=region, puuid=puuid, size=size
        )
    assert len(responses.calls) == 1
    validate_exception(error_response, excinfo)

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, "get_match_history_by_puuid")(
            version=version, region=region, puuid=puuid, size=size
        )
    assert len(responses.calls) == 2
    validate_exception(error_response, excinfo)

    with aioresponses() as m:
        m.get(url, payload=error_response, exception=ValoAPIException(error_response))
        m.get(
            f"{url}?size={size}",
            payload=error_response,
            exception=ValoAPIException(error_response),
        )
        with pytest.raises(ValoAPIException) as excinfo:
            await getattr(valo_api, f"get_match_history_by_puuid_{version}_async")(
                region=region, puuid=puuid, size=size
            )
            validate_exception(error_response, excinfo)
        m.assert_called_once()

    with aioresponses() as m:
        m.get(url, payload=error_response, exception=ValoAPIException(error_response))
        m.get(
            f"{url}?size={size}",
            payload=error_response,
            exception=ValoAPIException(error_response),
        )
        with pytest.raises(ValoAPIException) as excinfo:
            await getattr(valo_api, "get_match_history_by_puuid_async")(
                version=version, region=region, puuid=puuid, size=size
            )
            validate_exception(error_response, excinfo)
        m.assert_called_once()


if __name__ == "__main__":
    test_get_match_history_by_name()
    test_get_match_history_by_name_error()
    test_get_match_history_by_puuid()
    test_get_match_history_by_puuid_error()
