from typing import Optional

from valo_api.utils.dict_struct import DictStruct


class MMRHistoryPointImagesV1(DictStruct):
    small: Optional[str] = None
    large: Optional[str] = None
    triangle_down: Optional[str] = None
    triangle_up: Optional[str] = None


class MMRHistoryPointMapV1(DictStruct):
    name: str
    id: str


class MMRHistoryPointV1(DictStruct):
    currenttier: int
    currenttierpatched: str
    images: MMRHistoryPointImagesV1
    match_id: str
    map: MMRHistoryPointMapV1
    season_id: str
    ranking_in_tier: int
    mmr_change_to_last_game: int
    elo: int
    date: str
    date_raw: int
