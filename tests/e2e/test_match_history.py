from typing import Optional

from time import sleep
from uuid import UUID

from hypothesis import given, settings
from hypothesis import strategies as st

import valo_api
from valo_api.exceptions.rate_limit import rate_limit


@settings(deadline=None, max_examples=15)
@given(
    version=st.sampled_from(["v3"]),
    id=st.sampled_from(["ManuelHexe#5777", "jasminaxrose#7024"]),
    size=st.one_of(st.none(), st.integers(min_value=1, max_value=5)),
)
def test_get_match_history_by_name(version: str, id: str, size: Optional[int]):
    sleep(rate_limit().reset + 1 if rate_limit().remaining <= 2 else 0)
    print(f"Test get_match_history_by_name with: {locals()}")

    name, tag = id.split("#")

    getattr(valo_api, f"get_match_history_by_name_{version}")(
        region="eu", name=name, tag=tag, size=size
    )


@settings(deadline=None, max_examples=15)
@given(
    version=st.sampled_from(["v3"]),
    puuid=st.sampled_from(
        ["ee89b4d9-13d0-5832-8dd7-eb5d8806d918", "930bb0d3-c914-5394-bcf6-0bc81f465bd7"]
    ),
    size=st.one_of(st.none(), st.integers(min_value=1, max_value=5)),
)
def test_get_match_history_by_puuid(version: str, puuid: UUID, size: Optional[int]):
    sleep(rate_limit().reset + 1 if rate_limit().remaining <= 2 else 0)
    print(f"Test get_match_history_by_puuid with: {locals()}")

    getattr(valo_api, f"get_match_history_by_puuid_{version}")(
        region="eu", puuid=puuid, size=size
    )


if __name__ == "__main__":
    test_get_match_history_by_name()
    test_get_match_history_by_puuid()
