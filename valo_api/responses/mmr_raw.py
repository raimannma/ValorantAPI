from typing import Dict

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
    SeasonalInfoBySeasonID: Dict[str, SeasonInfoRaw]

    def __post_init__(self):
        self.SeasonalInfoBySeasonID = {
            k: SeasonInfoRaw.from_dict(**v)
            for k, v in self.SeasonalInfoBySeasonID.items()
        }


@dataclass
class QueueSkills(InitOptions):
    competitive: QueueSkill
    custom: QueueSkill
    deathmatch: QueueSkill
    onefa: QueueSkill
    seeding: QueueSkill
    spikerush: QueueSkill
    unrated: QueueSkill

    def __post_init__(self):
        self.competitive = QueueSkill.from_dict(**self.competitive)
        self.custom = QueueSkill.from_dict(**self.custom)
        self.deathmatch = QueueSkill.from_dict(**self.deathmatch)
        self.onefa = QueueSkill.from_dict(**self.onefa)
        self.seeding = QueueSkill.from_dict(**self.seeding)
        self.spikerush = QueueSkill.from_dict(**self.spikerush)
        self.unrated = QueueSkill.from_dict(**self.unrated)


@dataclass
class MMRRawV1(InitOptions):
    Version: int
    Subject: str
    NewPlayerExperienceFinished: bool
    QueueSkills: QueueSkills
    LatestCompetitiveUpdate: CompetitiveMatchRaw
    IsLeaderboardAnonymized: bool
    IsActRankBadgeHidden: bool

    def __post_init__(self):
        self.QueueSkills = QueueSkills.from_dict(**self.QueueSkills)
        self.LatestCompetitiveUpdate = CompetitiveMatchRaw.from_dict(
            **self.LatestCompetitiveUpdate
        )
