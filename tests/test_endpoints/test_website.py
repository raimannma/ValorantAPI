import responses
from hypothesis import given
from hypothesis import strategies as st

import valo_api
from tests.test_endpoints.utils import get_mock_response
from valo_api.config import Config


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


if __name__ == "__main__":
    test_get_website()
