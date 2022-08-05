from time import sleep

from hypothesis import given, settings
from hypothesis import strategies as st

import valo_api
from valo_api.exceptions.rate_limit import rate_limit


@settings(deadline=None, max_examples=15)
@given(
    version=st.sampled_from(["v1"]),
    crosshair_id=st.sampled_from(["0;P;h;0;f;0;0l;4;0o;0;0a;1;0f;0;1b;0"]),
)
def test_get_crosshair(version: str, crosshair_id: str):
    sleep(rate_limit().reset + 1 if rate_limit().remaining <= 2 else 0)
    print(f"Test get_crosshair with: {locals()}")

    getattr(valo_api, f"get_crosshair_{version}")(crosshair_id=crosshair_id)


if __name__ == "__main__":
    test_get_crosshair()
