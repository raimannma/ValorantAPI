from typing import List, Optional

from valo_api.utils.dict_struct import DictStruct


class LeaderboardPlayerV1(DictStruct):
    PlayerCardID: str
    TitleID: str
    IsBanned: bool
    IsAnonymized: bool
    puuid: str
    gameName: str
    tagLine: str
    leaderboardRank: int
    rankedRating: int
    numberOfWins: int
    competitiveTier: int


class LeaderboardPlayerV2(DictStruct):
    PlayerCardID: str
    TitleID: str
    IsBanned: bool
    IsAnonymized: bool
    puuid: str
    gameName: str
    tagLine: str
    leaderboardRank: int
    rankedRating: int
    numberOfWins: int
    competitiveTier: int


class LeaderboardV2(DictStruct):
    total_players: int
    radiant_threshold: int
    immortal_3_threshold: int
    immortal_2_threshold: int
    immortal_1_threshold: int
    players: List[Optional[LeaderboardPlayerV2]]
    last_update: Optional[int] = None
    next_update: Optional[int] = None
