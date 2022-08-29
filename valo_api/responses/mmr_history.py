from msgspec import Struct


class MMRHistoryPointV1(Struct):
    currenttier: int
    currenttierpatched: str
    ranking_in_tier: int
    mmr_change_to_last_game: int
    elo: int
    date: str
    date_raw: int
