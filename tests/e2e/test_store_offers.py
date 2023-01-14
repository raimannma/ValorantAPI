from time import sleep

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

import valo_api
from tests.e2e import new_event_loop_decorator
from valo_api.exceptions.rate_limit import rate_limit


@settings(deadline=None, max_examples=15)
@given(version=st.sampled_from(["v1", "v2"]))
@pytest.mark.asyncio
@new_event_loop_decorator
async def test_get_store_offers(version: str):
    sleep(rate_limit().reset + 1 if rate_limit().remaining <= 2 else 0)
    print(f"Test get_store_offers with: {locals()}")

    getattr(valo_api, f"get_store_offers_{version}")()

    try:
        await getattr(valo_api, f"get_store_offers_{version}_async")()
    except RuntimeError:
        pass


if __name__ == "__main__":
    test_get_store_offers()
