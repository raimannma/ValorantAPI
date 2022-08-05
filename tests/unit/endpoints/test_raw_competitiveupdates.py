from uuid import UUID

import responses
from hypothesis import given
from hypothesis import strategies as st

import valo_api
from tests.unit.endpoints.utils import get_mock_response
from valo_api.config import Config
from valo_api.endpoints.raw import EndpointType


@given(
    version=st.sampled_from(["v1"]),
    puuid=st.uuids(),
    region=st.sampled_from(Config.ALL_REGIONS),
)
@responses.activate
def test_get_raw_competitiveupdates(version: str, puuid: UUID, region: str):
    print(f"Test get_raw_competitiveupdates with: {locals()}")

    url = f"{Config.BASE_URL}/valorant/{version}/raw"

    puuid = str(puuid).lower()

    responses.add(
        responses.POST,
        url,
        json=get_mock_response(f"raw_competitiveupdates_{version}.json"),
        status=200,
    )

    getattr(valo_api, f"get_raw_data_{version}")(
        type=EndpointType.COMPETITIVE_UPDATES, region=region, value=puuid
    )
    assert len(responses.calls) == 1

    getattr(valo_api, "get_raw_data")(
        version=version,
        type=EndpointType.COMPETITIVE_UPDATES,
        region=region,
        value=puuid,
    )
    assert len(responses.calls) == 2


if __name__ == "__main__":
    test_get_raw_competitiveupdates()
