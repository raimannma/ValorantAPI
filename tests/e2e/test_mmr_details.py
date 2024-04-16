from typing import Optional

from time import sleep

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

import valo_api
from valo_api.exceptions.rate_limit import rate_limit


@settings(deadline=None, max_examples=15)
@given(
    version=st.sampled_from(["v2"]),
    id=st.sampled_from(["ManuelHexe#5777", "jasminaxrose#7024"]),
)
@pytest.mark.asyncio
async def test_get_mmr_details_by_name(version: str, id: str):
    sleep(rate_limit().reset + 1 if rate_limit().remaining <= 2 else 0)
    print(f"Test get_mmr_details_by_name with: {locals()}")

    name, tag = id.split("#")

    getattr(valo_api, f"get_mmr_details_by_name_{version}")(
        region="eu", name=name, tag=tag
    )

    try:
        await getattr(valo_api, f"get_mmr_details_by_name_{version}_async")(
            region="eu", name=name, tag=tag
        )
    except RuntimeError:
        pass


@settings(deadline=None, max_examples=15)
@given(
    version=st.sampled_from(["v2"]),
    puuid=st.sampled_from(
        ["ee89b4d9-13d0-5832-8dd7-eb5d8806d918", "930bb0d3-c914-5394-bcf6-0bc81f465bd7"]
    ),
)
@pytest.mark.asyncio
async def test_get_mmr_details_by_puuid(version: str, puuid: str):
    sleep(rate_limit().reset + 1 if rate_limit().remaining <= 2 else 0)
    print(f"Test get_mmr_details_by_puuid with: {locals()}")

    getattr(valo_api, f"get_mmr_details_by_puuid_{version}")(region="eu", puuid=puuid)

    try:
        getattr(valo_api, f"get_mmr_details_by_puuid_{version}_async")(
            region="eu", puuid=puuid
        )
    except RuntimeError:
        pass


if __name__ == "__main__":
    test_get_mmr_details_by_name()
    test_get_mmr_details_by_puuid()
