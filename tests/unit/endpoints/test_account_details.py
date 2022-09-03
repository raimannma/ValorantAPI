import urllib.parse

import pytest
import responses
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
    force_update=st.booleans(),
)
@responses.activate
def test_get_account_details_by_name(
    version: str, name: str, tag: str, force_update: bool
):
    print(f"Test get_account_details_by_name with: {locals()}")

    encoded_name = urllib.parse.quote_plus(name).lower()
    encoded_tag = urllib.parse.quote_plus(tag).lower()

    url = f"{Config.BASE_URL}/valorant/{version}/account/{encoded_name}/{encoded_tag}"
    params = {"force": str(force_update).lower()}

    responses.add(
        responses.GET,
        url,
        match=[matchers.query_param_matcher(params)],
        json=get_mock_response(f"account_details_{version}.json"),
        status=200,
    )

    getattr(valo_api, f"get_account_details_by_name_{version}")(
        name=name, tag=tag, force_update=force_update
    )
    assert len(responses.calls) == 1

    getattr(valo_api, "get_account_details_by_name")(
        version=version, name=name, tag=tag, force_update=force_update
    )
    assert len(responses.calls) == 2


@given(
    version=st.sampled_from(["v1"]),
    name=st.text(),
    tag=st.text(),
    force_update=st.booleans(),
    error_response=st.sampled_from(get_error_responses("account_details")),
)
@responses.activate
def test_get_account_details_by_name_error(
    version: str, name: str, tag: str, force_update: bool, error_response: dict
):
    print(f"Test get_account_details_by_name_error with: {locals()}")

    encoded_name = urllib.parse.quote_plus(name).lower()
    encoded_tag = urllib.parse.quote_plus(tag).lower()

    url = f"{Config.BASE_URL}/valorant/{version}/account/{encoded_name}/{encoded_tag}"
    params = {"force": str(force_update).lower()}

    responses.add(
        responses.GET,
        url,
        match=[matchers.query_param_matcher(params)],
        json=error_response,
        status=int(error_response["status"]) if "status" in error_response else 500,
    )

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, f"get_account_details_by_name_{version}")(
            name=name, tag=tag, force_update=force_update
        )
    assert len(responses.calls) == 1
    validate_exception(error_response, excinfo)

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, "get_account_details_by_name")(
            version=version, name=name, tag=tag, force_update=force_update
        )
    assert len(responses.calls) == 2
    validate_exception(error_response, excinfo)


@given(
    version=st.sampled_from(["v1"]),
    puuid=st.uuids(),
    force_update=st.booleans(),
)
@responses.activate
def test_get_account_details_by_puuid(version: str, puuid: str, force_update: bool):
    print(f"Test get_account_details_by_puuid with: {locals()}")

    puuid = str(puuid).lower()

    url = f"{Config.BASE_URL}/valorant/{version}/by-puuid/account/{puuid}"
    params = {"force": str(force_update).lower()}

    responses.add(
        responses.GET,
        url,
        match=[matchers.query_param_matcher(params)],
        json=get_mock_response(f"account_details_{version}.json"),
        status=200,
    )

    getattr(valo_api, f"get_account_details_by_puuid_{version}")(
        puuid=puuid, force_update=force_update
    )
    assert len(responses.calls) == 1

    getattr(valo_api, "get_account_details_by_puuid")(
        version=version, puuid=puuid, force_update=force_update
    )
    assert len(responses.calls) == 2


@given(
    version=st.sampled_from(["v1"]),
    puuid=st.uuids(),
    force_update=st.booleans(),
    error_response=st.sampled_from(get_error_responses("account_details")),
)
@responses.activate
def test_get_account_details_by_puuid_error(
    version: str, puuid: str, force_update: bool, error_response: dict
):
    print(f"Test get_account_details_by_puuid_error with: {locals()}")

    puuid = str(puuid).lower()

    url = f"{Config.BASE_URL}/valorant/{version}/by-puuid/account/{puuid}"
    params = {"force": str(force_update).lower()}

    responses.add(
        responses.GET,
        url,
        match=[matchers.query_param_matcher(params)],
        json=error_response,
        status=int(error_response["status"]) if "status" in error_response else 500,
    )

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, f"get_account_details_by_puuid_{version}")(
            puuid=puuid, force_update=force_update
        )
    assert len(responses.calls) == 1
    validate_exception(error_response, excinfo)

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, "get_account_details_by_puuid")(
            version=version, puuid=puuid, force_update=force_update
        )
    assert len(responses.calls) == 2
    validate_exception(error_response, excinfo)


if __name__ == "__main__":
    test_get_account_details_by_name()
    test_get_account_details_by_name_error()
    test_get_account_details_by_puuid()
    test_get_account_details_by_puuid_error()
