from typing import List, Optional

from valo_api.utils.dict_struct import DictStruct

class LeaderboardPlayerV2(DictStruct):
    PlayerCardID: str
    TitleID: str
    IsBanned: bool
    IsAnonymized: bool
    puuid: Optional[str]
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

class LeaderboardThresholdTierV3(DictStruct):
    id: int
    name: str

class LeaderboardThresholdV3(DictStruct):
    tier: LeaderboardThresholdTierV3
    start_index: int
    threshold: int

class LeaderboardResultsV3(DictStruct):
    total: int
    returned: int
    before: int
    after: int

class LeaderboardPlayerV3(DictStruct):
    card: str
    title: str
    is_banned: bool
    is_anonymized: bool
    puuid: Optional[str]
    name: str
    tag: str
    leaderboard_rank: int
    tier: int
    rr: int
    wins: int
    updated_at: str

class LeaderboardDataV3(DictStruct):
    updated_at: str
    thresholds: List[LeaderboardThresholdV3]
    players: List[Optional[LeaderboardPlayerV3]]

class LeaderboardV3(DictStruct):
    status: int
    results: LeaderboardResultsV3
    data: LeaderboardDataV3
