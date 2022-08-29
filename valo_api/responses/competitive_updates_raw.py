from typing import List

from msgspec import Struct


class CompetitiveMatchRaw(Struct):
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


class CompetitiveUpdatesRawV1(Struct):
    Version: int
    Subject: str
    Matches: List[CompetitiveMatchRaw]
