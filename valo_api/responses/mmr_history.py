from dataclasses import dataclass

from valo_api.utils.init_options import InitOptions


@dataclass
class MMRHistoryPointV1(InitOptions):
    currenttier: int
    currenttierpatched: str
    ranking_in_tier: int
    mmr_change_to_last_game: int
    elo: int
    date: str
    date_raw: int
