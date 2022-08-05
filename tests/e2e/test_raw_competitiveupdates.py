from time import sleep

from hypothesis import given, settings
from hypothesis import strategies as st

import valo_api
from valo_api.config import Config
from valo_api.endpoints.raw import EndpointType
from valo_api.exceptions.rate_limit import rate_limit


@settings(deadline=None, max_examples=15)
@given(
    version=st.sampled_from(["v1"]),
    puuid=st.sampled_from(
        ["ee89b4d9-13d0-5832-8dd7-eb5d8806d918", "930bb0d3-c914-5394-bcf6-0bc81f465bd7"]
    ),
    region=st.sampled_from(Config.ALL_REGIONS),
)
def test_get_raw_competitiveupdates(version: str, puuid: str, region: str):
    sleep(rate_limit().reset + 1 if rate_limit().remaining <= 2 else 0)
    print(f"Test get_raw_competitiveupdates with: {locals()}")

    getattr(valo_api, f"get_raw_data_{version}")(
        type=EndpointType.COMPETITIVE_UPDATES, region=region, value=puuid
    )


if __name__ == "__main__":
    test_get_raw_competitiveupdates()
