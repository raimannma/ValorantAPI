from typing import Dict, Optional

from dataclasses import dataclass

from valo_api.responses.competitive_updates_raw import CompetitiveMatchRaw
from valo_api.utils.init_options import InitOptions


@dataclass
class SeasonInfoRaw(InitOptions):
    SeasonID: str
    NumberOfWins: int
    NumberOfWinsWithPlacements: int
    NumberOfGames: int
    Rank: int
    CapstoneWins: int
    LeaderboardRank: int
    CompetitiveTier: int
    RankedRating: int
    WinsByTier: Dict[str, int]
    GamesNeededForRating: int
    TotalWinsNeededForRank: int


@dataclass
class QueueSkill(InitOptions):
    TotalGamesNeededForRating: int
    TotalGamesNeededForLeaderboard: int
    CurrentSeasonGamesNeededForRating: int
    SeasonalInfoBySeasonID: Optional[Dict[str, SeasonInfoRaw]]

    def __post_init__(self):
        self.SeasonalInfoBySeasonID = (
            {
                k: SeasonInfoRaw.from_dict(**v)
                for k, v in self.SeasonalInfoBySeasonID.items()
            }
            if self.SeasonalInfoBySeasonID
            else None
        )


@dataclass
class QueueSkills(InitOptions):
    competitive: Optional[QueueSkill] = None
    custom: Optional[QueueSkill] = None
    deathmatch: Optional[QueueSkill] = None
    onefa: Optional[QueueSkill] = None
    seeding: Optional[QueueSkill] = None
    spikerush: Optional[QueueSkill] = None
    unrated: Optional[QueueSkill] = None

    def __post_init__(self):
        self.competitive = (
            QueueSkill.from_dict(**self.competitive) if self.competitive else None
        )
        self.custom = QueueSkill.from_dict(**self.custom) if self.custom else None
        self.deathmatch = (
            QueueSkill.from_dict(**self.deathmatch) if self.deathmatch else None
        )
        self.onefa = QueueSkill.from_dict(**self.onefa) if self.onefa else None
        self.seeding = QueueSkill.from_dict(**self.seeding) if self.seeding else None
        self.spikerush = (
            QueueSkill.from_dict(**self.spikerush) if self.spikerush else None
        )
        self.unrated = QueueSkill.from_dict(**self.unrated) if self.unrated else None


@dataclass
class MMRRawV1(InitOptions):
    Version: int
    Subject: str
    NewPlayerExperienceFinished: bool
    QueueSkills: QueueSkills
    LatestCompetitiveUpdate: Optional[CompetitiveMatchRaw]
    IsLeaderboardAnonymized: bool
    IsActRankBadgeHidden: bool

    def __post_init__(self):
        self.QueueSkills = QueueSkills.from_dict(**self.QueueSkills)
        self.LatestCompetitiveUpdate = (
            CompetitiveMatchRaw.from_dict(**self.LatestCompetitiveUpdate)
            if self.LatestCompetitiveUpdate
            else None
        )
