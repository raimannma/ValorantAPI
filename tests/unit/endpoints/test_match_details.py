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
    version=st.sampled_from(["v2"]),
    match_id=st.uuids(),
)
@responses.activate
@pytest.mark.asyncio
async def test_get_match_details(version: str, match_id: UUID):
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

    getattr(valo_api, f"get_match_details_{version}")(match_id=match_id)
    assert len(responses.calls) == 1

    getattr(valo_api, "get_match_details")(version=version, match_id=match_id)
    assert len(responses.calls) == 2

    with aioresponses() as m:
        m.get(url, payload=get_mock_response(f"match_details_{version}.json"))
        await getattr(valo_api, f"get_match_details_{version}_async")(match_id=match_id)
        m.assert_called_once()

    with aioresponses() as m:
        m.get(url, payload=get_mock_response(f"match_details_{version}.json"))
        await getattr(valo_api, "get_match_details_async")(
            version=version, match_id=match_id
        )
        m.assert_called_once()


@given(
    version=st.sampled_from(["v2"]),
    match_id=st.uuids(),
    error_response=st.sampled_from(get_error_responses("match_details")),
)
@responses.activate
@pytest.mark.asyncio
async def test_get_match_details_error(
    version: str, match_id: UUID, error_response: dict
):
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
        getattr(valo_api, f"get_match_details_{version}")(match_id=match_id)
        validate_exception(error_response, excinfo)
    assert len(responses.calls) == 1

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, "get_match_details")(version=version, match_id=match_id)
        validate_exception(error_response, excinfo)
    assert len(responses.calls) == 2

    with aioresponses() as m:
        m.get(url, payload=error_response, exception=ValoAPIException(error_response))
        with pytest.raises(ValoAPIException) as excinfo:
            await getattr(valo_api, f"get_match_details_{version}_async")(
                match_id=match_id
            )
            validate_exception(error_response, excinfo)
        m.assert_called_once()

    with aioresponses() as m:
        m.get(url, payload=error_response, exception=ValoAPIException(error_response))
        with pytest.raises(ValoAPIException) as excinfo:
            await getattr(valo_api, "get_match_details_async")(
                version=version, match_id=match_id
            )
            validate_exception(error_response, excinfo)
        m.assert_called_once()


if __name__ == "__main__":
    test_get_match_details()
    test_get_match_details_error()
