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
@given(version=st.sampled_from(["v1"]), locale=st.sampled_from(Config.ALL_LOCALS))
@responses.activate
@pytest.mark.asyncio
async def test_get_content(version: str, locale: str):
    print(f"Test get_content with: {locals()}")

    locale = str(locale).lower()

    url = f"{Config.BASE_URL}/valorant/{version}/content"
    params = {"locale": locale}

    responses.add(
        responses.GET,
        url,
        match=[matchers.query_param_matcher(params)],
        json=get_mock_response(f"content_{version}.json"),
        status=200,
    )

    getattr(valo_api, f"get_content_{version}")(locale=locale)
    assert len(responses.calls) == 1

    getattr(valo_api, "get_content")(version=version, locale=locale)
    assert len(responses.calls) == 2

    with aioresponses() as m:
        m.get(
            f"{url}?locale={locale}",
            payload=get_mock_response(f"content_{version}.json"),
            status=200,
        )

        await getattr(valo_api, f"get_content_{version}_async")(locale=locale)
        m.assert_called_once()

    with aioresponses() as m:
        m.get(
            f"{url}?locale={locale}",
            payload=get_mock_response(f"content_{version}.json"),
            status=200,
        )

        await getattr(valo_api, "get_content_async")(version=version, locale=locale)
        m.assert_called_once()


@given(
    version=st.sampled_from(["v1"]),
    locale=st.sampled_from(Config.ALL_LOCALS),
    error_response=st.sampled_from(get_error_responses("content")),
)
@responses.activate
@pytest.mark.asyncio
async def test_get_content_error(version: str, locale: str, error_response: dict):
    print(f"Test get_content with: {locals()}")

    locale = str(locale).lower()

    url = f"{Config.BASE_URL}/valorant/{version}/content"
    params = {"locale": locale}

    responses.add(
        responses.GET,
        url,
        match=[matchers.query_param_matcher(params)],
        json=error_response,
        status=int(error_response["status"]) if "status" in error_response else 500,
    )

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, f"get_content_{version}")(locale=locale)
        validate_exception(error_response, excinfo)
    assert len(responses.calls) == 1

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, "get_content")(version=version, locale=locale)
        validate_exception(error_response, excinfo)
    assert len(responses.calls) == 2

    with aioresponses() as m:
        m.get(
            f"{url}?locale={locale}",
            exception=ValoAPIException(error_response),
            repeat=True,
        )

        with pytest.raises(ValoAPIException) as excinfo:
            await getattr(valo_api, f"get_content_{version}_async")(locale=locale)
            validate_exception(error_response, excinfo)
        m.assert_called_once()

    with aioresponses() as m:
        m.get(
            f"{url}?locale={locale}",
            exception=ValoAPIException(error_response),
            repeat=True,
        )

        with pytest.raises(ValoAPIException) as excinfo:
            await getattr(valo_api, "get_content_async")(version=version, locale=locale)
            validate_exception(error_response, excinfo)
        m.assert_called_once()


if __name__ == "__main__":
    test_get_content()
    test_get_content_error()
