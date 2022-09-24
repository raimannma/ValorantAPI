from typing import List

from valo_api.utils.dict_struct import DictStruct


class CompetitiveMatchRaw(DictStruct):
    MatchID: str
    MapID: str
    SeasonID: str
    MatchStartTime: int
    TierAfterUpdate: int
    TierBeforeUpdate: int
    RankedRatingAfterUpdate: int
    RankedRatingBeforeUpdate: int
    RankedRatingEarned: int
    RankedRatingPerformanceBonus: int
    CompetitiveMovement: str
    AFKPenalty: int


class CompetitiveUpdatesRawV1(DictStruct):
    Version: int
    Subject: str
    Matches: List[CompetitiveMatchRaw]
