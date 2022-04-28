import responses
from hypothesis import given
from hypothesis import strategies as st

import valo_api
from tests.test_endpoints.utils import get_mock_response
from valo_api.config import Config


@given(version=st.sampled_from(["v1"]))
@responses.activate
def test_get_store_offers(version: str):
    print(f"Test get_store_offers with: {locals()}")

    url = f"{Config.BASE_URL}/valorant/{version}/store-offers"

    responses.add(
        responses.GET,
        url,
        json=get_mock_response(f"store_offers_{version}.json"),
        status=200,
    )

    getattr(valo_api, f"get_store_offers_{version}")()
    assert len(responses.calls) == 1

    getattr(valo_api, "get_store_offers")(version=version)
    assert len(responses.calls) == 2


if __name__ == "__main__":
    test_get_store_offers()
