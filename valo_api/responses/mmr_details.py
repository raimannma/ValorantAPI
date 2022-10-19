from typing import Dict, List, Optional

from valo_api.utils.dict_struct import DictStruct


class MMRDetailsV1(DictStruct):
    name: str
    tag: str
    elo: int
    old: bool
    currenttier: Optional[int] = None
    currenttierpatched: Optional[str] = None
    ranking_in_tier: Optional[int] = None
    mmr_change_to_last_game: Optional[int] = None


class CurrentDataV2(DictStruct):
    old: bool
    currenttier: Optional[int] = None
    currenttierpatched: Optional[str] = None
    ranking_in_tier: Optional[int] = None
    mmr_change_to_last_game: Optional[int] = None
    elo: Optional[int] = None
    games_needed_for_rating: Optional[int] = None


class ActRankWinV2(DictStruct):
    patched_tier: str
    tier: int


class SeasonDataV2(DictStruct):
    wins: Optional[int] = None
    number_of_games: Optional[int] = None
    final_rank: Optional[int] = None
    final_rank_patched: Optional[str] = None
    act_rank_wins: Optional[List[ActRankWinV2]] = None
    old: Optional[bool] = None
    error: Optional[str] = None


class MMRDetailsV2(DictStruct):
    name: str
    tag: str
    current_data: CurrentDataV2
    by_season: Dict[str, SeasonDataV2]
