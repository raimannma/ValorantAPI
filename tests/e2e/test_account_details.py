from time import sleep

import pytest
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
@pytest.mark.asyncio
async def test_get_account_details_by_name(version: str, id: str, force_update: bool):
    sleep(rate_limit().reset + 1 if rate_limit().remaining <= 2 else 0)
    print(f"Test get_account_details with: {locals()}")

    name, tag = id.split("#")

    getattr(valo_api, f"get_account_details_by_name_{version}")(
        name=name, tag=tag, force_update=force_update
    )
    try:
        await getattr(valo_api, f"get_account_details_by_name_{version}_async")(
            name=name, tag=tag, force_update=force_update
        )
    except RuntimeError:
        pass


@settings(deadline=None, max_examples=15)
@given(
    version=st.sampled_from(["v1"]),
    puuid=st.sampled_from(
        ["ee89b4d9-13d0-5832-8dd7-eb5d8806d918", "930bb0d3-c914-5394-bcf6-0bc81f465bd7"]
    ),
    force_update=st.booleans(),
)
@pytest.mark.asyncio
async def test_get_account_details_by_puuid(
    version: str, puuid: str, force_update: bool
):
    sleep(rate_limit().reset + 1 if rate_limit().remaining <= 2 else 0)
    print(f"Test get_account_details with: {locals()}")

    getattr(valo_api, f"get_account_details_by_puuid_{version}")(
        puuid=puuid, force_update=force_update
    )

    try:
        await getattr(valo_api, f"get_account_details_by_puuid_{version}_async")(
            puuid=puuid, force_update=force_update
        )
    except RuntimeError:
        pass


if __name__ == "__main__":
    test_get_account_details_by_name()
    test_get_account_details_by_puuid()
