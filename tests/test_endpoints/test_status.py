import responses
from hypothesis import given
from hypothesis import strategies as st

import valo_api
from tests.test_endpoints.utils import get_mock_response
from valo_api.config import Config


@given(version=st.sampled_from(["v1"]), region=st.sampled_from(Config.ALL_REGIONS))
@responses.activate
def test_get_status(version: str, region: str):
    print(f"Test get_status with: {locals()}")

    url = f"{Config.BASE_URL}/valorant/{version}/status/{region}"

    responses.add(
        responses.GET,
        url,
        json=get_mock_response(f"status_{version}.json"),
        status=200,
    )

    getattr(valo_api, f"get_status_{version}")(region=region)
    assert len(responses.calls) == 1

    getattr(valo_api, "get_status")(version=version, region=region)
    assert len(responses.calls) == 2


if __name__ == "__main__":
    test_get_status()
