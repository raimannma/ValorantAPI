from valo_api.utils.dict_struct import DictStruct


class MMRHistoryPointV1(DictStruct):
    currenttier: int
    currenttierpatched: str
    ranking_in_tier: int
    mmr_change_to_last_game: int
    elo: int
    date: str
    date_raw: int
