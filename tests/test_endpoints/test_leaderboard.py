import urllib.parse

import responses
from hypothesis import given, settings
from hypothesis import strategies as st

import valo_api
from tests.test_endpoints.utils import get_mock_response
from valo_api.config import Config


@settings(deadline=None)
@given(
    version=st.sampled_from(["v1", "v2"]), region=st.sampled_from(Config.ALL_REGIONS)
)
@responses.activate
def test_get_leaderboard(version: str, region: str):
    print(f"Test get_leaderboard with: {locals()}")

    encoded_region = urllib.parse.quote_plus(region).lower()

    url = f"{Config.BASE_URL}/valorant/{version}/leaderboard/{encoded_region}"

    responses.add(
        responses.GET,
        url,
        json=get_mock_response(f"leaderboard_{version}.json"),
        status=200,
    )

    getattr(valo_api, f"get_leaderboard_{version}")(region=region)
    assert len(responses.calls) == 1

    getattr(valo_api, "get_leaderboard")(version=version, region=region)
    assert len(responses.calls) == 2


if __name__ == "__main__":
    test_get_leaderboard()
