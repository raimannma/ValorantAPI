from time import sleep

from hypothesis import given, settings
from hypothesis import strategies as st

import valo_api
from valo_api.exceptions.rate_limit import rate_limit


@settings(deadline=None, max_examples=15)
@given(version=st.sampled_from(["v1", "v2"]))
def test_get_store_featured(version: str):
    sleep(rate_limit().reset + 1 if rate_limit().remaining <= 2 else 0)
    print(f"Test get_store_featured with: {locals()}")

    getattr(valo_api, f"get_store_featured_{version}")()


if __name__ == "__main__":
    test_get_store_featured()
