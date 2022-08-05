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
    version=st.sampled_from(["v1"]),
    countrycode=st.sampled_from(Config.ALL_COUNTRY_CODES),
)
@responses.activate
def test_get_website(version: str, countrycode: str):
    print(f"Test get_website with: {locals()}")

    url = f"{Config.BASE_URL}/valorant/{version}/website/{countrycode}"

    responses.add(
        responses.GET,
        url,
        json=get_mock_response(f"website_{version}.json"),
        status=200,
    )

    getattr(valo_api, f"get_website_{version}")(countrycode=countrycode)
    assert len(responses.calls) == 1

    getattr(valo_api, "get_website")(version=version, countrycode=countrycode)
    assert len(responses.calls) == 2


@given(
    version=st.sampled_from(["v1"]),
    countrycode=st.sampled_from(Config.ALL_COUNTRY_CODES),
    error_response=st.sampled_from(get_error_responses("website")),
)
@responses.activate
def test_get_website_error(version: str, countrycode: str, error_response: dict):
    print(f"Test test_get_version_info_error with: {locals()}")

    url = f"{Config.BASE_URL}/valorant/{version}/website/{countrycode}"

    responses.add(
        responses.GET,
        url,
        json=error_response,
        status=int(error_response["status"]) if "status" in error_response else 500,
    )

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, f"get_website_{version}")(countrycode=countrycode)
    assert len(responses.calls) == 1
    validate_exception(error_response, excinfo)

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, "get_website")(version=version, countrycode=countrycode)
    assert len(responses.calls) == 2
    validate_exception(error_response, excinfo)


if __name__ == "__main__":
    test_get_website()
    test_get_website_error()
