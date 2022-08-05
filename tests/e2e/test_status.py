from time import sleep

from hypothesis import given, settings
from hypothesis import strategies as st

import valo_api
from valo_api.config import Config
from valo_api.exceptions.rate_limit import rate_limit


@settings(deadline=None, max_examples=15)
@given(version=st.sampled_from(["v1"]), region=st.sampled_from(Config.ALL_REGIONS))
def test_get_status(version: str, region: str):
    sleep(rate_limit().reset + 1 if rate_limit().remaining <= 2 else 0)
    print(f"Test get_status with: {locals()}")

    getattr(valo_api, f"get_status_{version}")(region=region)


if __name__ == "__main__":
    test_get_status()
