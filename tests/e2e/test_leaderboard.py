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
    version=st.sampled_from(["v1", "v2"]),
    region=st.sampled_from(Config.ALL_REGIONS),
    episode=st.one_of(st.integers(3, 4), st.none()),
    act=st.one_of(st.integers(1, 3), st.none()),
)
@pytest.mark.asyncio
@new_event_loop_decorator
async def test_get_leaderboard(version: str, region: str, episode: int, act: int):
    sleep(rate_limit().reset + 1 if rate_limit().remaining <= 2 else 0)
    print(f"Test get_leaderboard with: {locals()}")

    season_id = f"e{episode}a{act}" if episode is not None and act is not None else None

    getattr(valo_api, f"get_leaderboard_{version}")(region=region, season_id=season_id)

    try:
        await getattr(valo_api, f"get_leaderboard_{version}_async")(
            region=region, season_id=season_id
        )
    except RuntimeError:
        pass


if __name__ == "__main__":
    test_get_leaderboard()
