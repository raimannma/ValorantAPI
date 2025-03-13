from typing import List, Optional

from valo_api.utils.dict_struct import DictStruct


class LeaderboardPlayerV1(DictStruct):
    PlayerCardID: str
    TitleID: str
    IsBanned: bool
    IsAnonymized: bool
    leaderboardRank: int
    rankedRating: int
    numberOfWins: int
    competitiveTier: int
    puuid: Optional[str] = None
    gameName: Optional[str] = None
    tagLine: Optional[str] = None


class LeaderboardPlayerV2(DictStruct):
    PlayerCardID: str
    TitleID: str
    IsBanned: bool
    IsAnonymized: bool
    leaderboardRank: int
    rankedRating: int
    numberOfWins: int
    competitiveTier: int
    puuid: Optional[str] = None
    gameName: Optional[str] = None
    tagLine: Optional[str] = None


class LeaderboardV2(DictStruct):
    radiant_threshold: Optional[int] = None
    immortal_3_threshold: Optional[int] = None
    immortal_2_threshold: Optional[int] = None
    immortal_1_threshold: Optional[int] = None
    players: Optional[List[Optional[LeaderboardPlayerV2]]] = None
    total_players: Optional[int] = None
    last_update: Optional[int] = None
    next_update: Optional[int] = None
