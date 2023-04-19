from typing import Optional

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
    id=st.sampled_from(["ManuelHexe#5777", "jasminaxrose#7024"]),
    mode=st.one_of(st.none(), st.sampled_from(["competitive", "unrated"])),
    map=st.one_of(st.none(), st.sampled_from(["Ascent", "Bind", "Haven", "Split"])),
    page=st.one_of(st.none(), st.integers(min_value=1, max_value=100)),
    size=st.one_of(st.none(), st.integers(min_value=1, max_value=100)),
)
@pytest.mark.asyncio
@new_event_loop_decorator
async def test_get_lifetime_matches_by_name(
    version: str,
    id: str,
    mode: Optional[str],
    map: Optional[str],
    page: Optional[int],
    size: Optional[int],
):
    sleep(rate_limit().reset + 1 if rate_limit().remaining <= 2 else 0)
    print(f"Test get_lifetime_matches_by_name with: {locals()}")

    name, tag = id.split("#")

    kwargs = {}
    if mode:
        kwargs["mode"] = mode
    if map:
        kwargs["map"] = map
    if page:
        kwargs["page"] = page
        if not size:
            kwargs["size"] = 20
    if size:
        kwargs["size"] = size
        if not page:
            kwargs["page"] = 1

    getattr(valo_api, f"get_lifetime_matches_by_name_{version}")(
        region="eu", name=name, tag=tag, **kwargs
    )

    try:
        await getattr(valo_api, f"get_lifetime_matches_by_name_{version}_async")(
            region="eu", name=name, tag=tag, **kwargs
        )
    except RuntimeError:
        pass


@settings(deadline=None, max_examples=15)
@given(
    version=st.sampled_from(["v1"]),
    puuid=st.sampled_from(
        ["ee89b4d9-13d0-5832-8dd7-eb5d8806d918", "930bb0d3-c914-5394-bcf6-0bc81f465bd7"]
    ),
    mode=st.one_of(st.none(), st.sampled_from(["competitive", "unrated"])),
    map=st.one_of(st.none(), st.sampled_from(["Ascent", "Bind", "Haven", "Split"])),
    page=st.one_of(st.none(), st.integers(min_value=1, max_value=100)),
    size=st.one_of(st.none(), st.integers(min_value=1, max_value=100)),
)
@pytest.mark.asyncio
@new_event_loop_decorator
async def test_get_lifetime_matches_by_puuid(
    version: str,
    puuid: str,
    mode: Optional[str],
    map: Optional[str],
    page: Optional[int],
    size: Optional[int],
):
    sleep(rate_limit().reset + 1 if rate_limit().remaining <= 2 else 0)
    print(f"Test get_lifetime_matches_by_puuid with: {locals()}")

    kwargs = {}
    if mode:
        kwargs["mode"] = mode
    if map:
        kwargs["map"] = map
    if page:
        kwargs["page"] = page
        if not size:
            kwargs["size"] = 20
    if size:
        kwargs["size"] = size
        if not page:
            kwargs["page"] = 1

    print("eu", puuid, kwargs)

    getattr(valo_api, f"get_lifetime_matches_by_puuid_{version}")(
        region="eu", puuid=puuid, **kwargs
    )

    try:
        getattr(valo_api, f"get_lifetime_matches_by_puuid_{version}_async")(
            region="eu", puuid=puuid, **kwargs
        )
    except RuntimeError:
        pass


if __name__ == "__main__":
    test_get_lifetime_matches_by_name()
    test_get_lifetime_matches_by_puuid()
