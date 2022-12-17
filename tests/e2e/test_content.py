from time import sleep

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

import valo_api
from tests.e2e import new_event_loop_decorator
from valo_api.config import Config
from valo_api.exceptions.rate_limit import rate_limit


@settings(deadline=None, max_examples=15)
@given(version=st.sampled_from(["v1"]), locale=st.sampled_from(Config.ALL_LOCALS))
@pytest.mark.asyncio
@new_event_loop_decorator
async def test_get_content(version: str, locale: str):
    sleep(rate_limit().reset + 1 if rate_limit().remaining <= 3 else 0)
    print(f"Test get_content with: {locals()}")

    locale = str(locale).lower()

    getattr(valo_api, f"get_content_{version}")(locale=locale)
    try:
        await getattr(valo_api, f"get_content_{version}_async")(locale=locale)
    except RuntimeError:
        pass


if __name__ == "__main__":
    test_get_content()
