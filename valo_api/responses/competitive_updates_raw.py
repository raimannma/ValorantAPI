from typing import List

from dataclasses import dataclass

from valo_api.utils.init_options import InitOptions


@dataclass
class CompetitiveMatchRaw(InitOptions):
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


@dataclass
class CompetitiveUpdatesRawV1(InitOptions):
    Version: int
    Subject: str
    Matches: List[CompetitiveMatchRaw]

    def __post_init__(self):
        self.Matches = [CompetitiveMatchRaw.from_dict(**m) for m in self.Matches]
