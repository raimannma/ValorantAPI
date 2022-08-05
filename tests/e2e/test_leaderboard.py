from time import sleep

from hypothesis import given, settings
from hypothesis import strategies as st

import valo_api
from valo_api.config import Config
from valo_api.exceptions.rate_limit import rate_limit


@settings(deadline=None, max_examples=15)
@given(
    version=st.sampled_from(["v1", "v2"]),
    region=st.sampled_from(Config.ALL_REGIONS),
    episode=st.one_of(st.integers(3, 4), st.none()),
    act=st.one_of(st.integers(1, 3), st.none()),
)
def test_get_leaderboard(version: str, region: str, episode: int, act: int):
    sleep(rate_limit().reset + 1 if rate_limit().remaining <= 2 else 0)
    print(f"Test get_leaderboard with: {locals()}")

    season_id = f"e{episode}a{act}" if episode is not None and act is not None else None

    getattr(valo_api, f"get_leaderboard_{version}")(region=region, season_id=season_id)


if __name__ == "__main__":
    test_get_leaderboard()
