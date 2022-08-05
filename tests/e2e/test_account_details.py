from time import sleep

from hypothesis import given, settings
from hypothesis import strategies as st

import valo_api
from valo_api.exceptions.rate_limit import rate_limit


@settings(deadline=None, max_examples=15)
@given(
    version=st.sampled_from(["v1"]),
    id=st.sampled_from(["ManuelHexe#5777", "jasminaxrose#7024"]),
    force_update=st.booleans(),
)
def test_get_account_details(version: str, id: str, force_update: bool):
    sleep(rate_limit().reset + 1 if rate_limit().remaining <= 2 else 0)
    print(f"Test get_account_details with: {locals()}")

    name, tag = id.split("#")

    getattr(valo_api, f"get_account_details_{version}")(
        name=name, tag=tag, force_update=force_update
    )


if __name__ == "__main__":
    test_get_account_details()
