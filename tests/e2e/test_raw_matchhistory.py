from time import sleep

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

import valo_api
from tests.e2e import new_event_loop_decorator
from valo_api.endpoints.raw import EndpointType
from valo_api.exceptions.rate_limit import rate_limit


@settings(deadline=None, max_examples=15)
@given(
    version=st.sampled_from(["v1"]),
    match_id=st.sampled_from(
        ["ee89b4d9-13d0-5832-8dd7-eb5d8806d918", "930bb0d3-c914-5394-bcf6-0bc81f465bd7"]
    ),
)
@pytest.mark.asyncio
@new_event_loop_decorator
async def test_get_raw_matchhistory(version: str, match_id: str):
    sleep(rate_limit().reset + 1 if rate_limit().remaining <= 2 else 0)
    print(f"Test get_raw_matchhistory with: {locals()}")

    getattr(valo_api, f"get_raw_data_{version}")(
        type=EndpointType.MATCH_HISTORY, region="eu", value=match_id
    )

    try:
        await getattr(valo_api, f"get_raw_data_{version}_async")(
            type=EndpointType.MATCH_HISTORY, region="eu", value=match_id
        )
    except RuntimeError:
        pass


if __name__ == "__main__":
    test_get_raw_matchhistory()
