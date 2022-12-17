from time import sleep

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

import valo_api
from tests.e2e import new_event_loop_decorator
from valo_api.config import Config
from valo_api.exceptions.rate_limit import rate_limit


@settings(deadline=None, max_examples=15)
@given(
    version=st.sampled_from(["v1"]),
    countrycode=st.sampled_from(Config.ALL_COUNTRY_CODES),
)
@pytest.mark.asyncio
@new_event_loop_decorator
async def test_get_website(version: str, countrycode: str):
    sleep(rate_limit().reset + 1 if rate_limit().remaining <= 2 else 0)
    print(f"Test get_website with: {locals()}")

    getattr(valo_api, f"get_website_{version}")(countrycode=countrycode)

    try:
        await getattr(valo_api, f"get_website_{version}_async")(countrycode=countrycode)
    except RuntimeError:
        pass


if __name__ == "__main__":
    test_get_website()
