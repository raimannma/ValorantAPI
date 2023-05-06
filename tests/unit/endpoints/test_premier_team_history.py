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
    name=st.text(),
    tag=st.text(),
)
@responses.activate
@pytest.mark.asyncio
async def test_get_premier_team_history_by_name(version: str, name: str, tag: str):
    print(f"Test get_premier_team_history_by_name with: {locals()}")

    encoded_name = urllib.parse.quote_plus(name).lower()
    encoded_tag = urllib.parse.quote_plus(tag).lower()

    url = f"{Config.BASE_URL}/valorant/{version}/premier/{encoded_name}/{encoded_tag}/history"

    responses.add(
        responses.GET,
        url,
        json=get_mock_response(f"premier_team_history_by_name_{version}.json"),
        status=200,
    )

    getattr(valo_api, f"get_premier_team_history_by_name_{version}")(name=name, tag=tag)
    assert len(responses.calls) == 1

    getattr(valo_api, "get_premier_team_history_by_name")(
        version=version, name=name, tag=tag
    )
    assert len(responses.calls) == 2

    with aioresponses() as m:
        m.get(
            url,
            payload=get_mock_response(f"premier_team_history_by_name_{version}.json"),
        )
        await getattr(valo_api, f"get_premier_team_history_by_name_{version}_async")(
            name=name, tag=tag
        )
        m.assert_called_once()

    with aioresponses() as m:
        m.get(
            url,
            payload=get_mock_response(f"premier_team_history_by_name_{version}.json"),
        )
        await getattr(valo_api, "get_premier_team_history_by_name_async")(
            version=version, name=name, tag=tag
        )
        m.assert_called_once()


@given(
    version=st.sampled_from(["v1"]),
    name=st.text(),
    tag=st.text(),
    error_response=st.sampled_from(get_error_responses("mmr_details")),
)
@responses.activate
@pytest.mark.asyncio
async def test_get_premier_team_history_by_name_error(
    version: str,
    name: str,
    tag: str,
    error_response: dict,
):
    print(f"Test test_get_premier_team_history_by_name_error with: {locals()}")

    encoded_name = urllib.parse.quote_plus(name).lower()
    encoded_tag = urllib.parse.quote_plus(tag).lower()

    url = f"{Config.BASE_URL}/valorant/{version}/premier/{encoded_name}/{encoded_tag}/history"

    responses.add(
        responses.GET,
        url,
        json=error_response,
        status=int(error_response["status"]) if "status" in error_response else 500,
    )

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, f"get_premier_team_history_by_name_{version}")(
            name=name, tag=tag
        )
        validate_exception(error_response, excinfo)
    assert len(responses.calls) == 1

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, "get_premier_team_history_by_name")(
            version=version, name=name, tag=tag
        )
        validate_exception(error_response, excinfo)
    assert len(responses.calls) == 2

    with aioresponses() as m:
        m.get(url, exception=ValoAPIException(error_response))
        with pytest.raises(ValoAPIException) as excinfo:
            await getattr(
                valo_api, f"get_premier_team_history_by_name_{version}_async"
            )(name=name, tag=tag)
            validate_exception(error_response, excinfo)
        m.assert_called_once()

    with aioresponses() as m:
        m.get(url, exception=ValoAPIException(error_response))
        with pytest.raises(ValoAPIException) as excinfo:
            await getattr(valo_api, "get_premier_team_history_by_name_async")(
                version=version, name=name, tag=tag
            )
            validate_exception(error_response, excinfo)
        m.assert_called_once()


@given(
    version=st.sampled_from(["v1"]),
    id=st.uuids(),
)
@responses.activate
@pytest.mark.asyncio
async def test_get_premier_team_history_by_id(version: str, id: UUID):
    print(f"Test get_premier_team_history_by_id with: {locals()}")

    id = str(id).lower()

    url = f"{Config.BASE_URL}/valorant/{version}/premier/{id}/history"

    responses.add(
        responses.GET,
        url,
        json=get_mock_response(f"premier_team_history_by_id_{version}.json"),
        status=200,
    )

    getattr(valo_api, f"get_premier_team_history_by_id_{version}")(id=id)
    assert len(responses.calls) == 1

    getattr(valo_api, "get_premier_team_history_by_id")(version=version, id=id)
    assert len(responses.calls) == 2

    with aioresponses() as m:
        m.get(
            url, payload=get_mock_response(f"premier_team_history_by_id_{version}.json")
        )
        await getattr(valo_api, f"get_premier_team_history_by_id_{version}_async")(
            id=id
        )
        m.assert_called_once()

    with aioresponses() as m:
        m.get(
            url, payload=get_mock_response(f"premier_team_history_by_id_{version}.json")
        )
        await getattr(valo_api, "get_premier_team_history_by_id_async")(
            version=version, id=id
        )
        m.assert_called_once()


@given(
    version=st.sampled_from(["v1"]),
    id=st.uuids(),
    error_response=st.sampled_from(get_error_responses("mmr_details")),
)
@responses.activate
@pytest.mark.asyncio
async def test_get_premier_team_history_by_id_error(
    version: str,
    id: UUID,
    error_response: dict,
):
    print(f"Test test_get_premier_team_history_by_id_error with: {locals()}")

    url = f"{Config.BASE_URL}/valorant/{version}/premier/{id}/history"

    responses.add(
        responses.GET,
        url,
        json=error_response,
        status=int(error_response["status"]) if "status" in error_response else 500,
    )

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, f"get_premier_team_history_by_id_{version}")(id=id)
        validate_exception(error_response, excinfo)
    assert len(responses.calls) == 1

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, "get_premier_team_history_by_id")(version=version, id=id)
        validate_exception(error_response, excinfo)
    assert len(responses.calls) == 2

    with aioresponses() as m:
        m.get(url, exception=ValoAPIException(error_response))
        with pytest.raises(ValoAPIException) as excinfo:
            await getattr(valo_api, f"get_premier_team_history_by_id_{version}_async")(
                id=id
            )
            validate_exception(error_response, excinfo)
        m.assert_called_once()

    with aioresponses() as m:
        m.get(url, exception=ValoAPIException(error_response))
        with pytest.raises(ValoAPIException) as excinfo:
            await getattr(valo_api, "get_premier_team_history_by_id_async")(
                version=version, id=id
            )
            validate_exception(error_response, excinfo)
        m.assert_called_once()


if __name__ == "__main__":
    test_get_premier_team_history_by_name()
    test_get_premier_team_history_by_name_error()
    test_get_premier_team_history_by_id()
    test_get_premier_team_history_by_id_error()
