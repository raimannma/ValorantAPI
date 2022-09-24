from typing import Dict, Optional

from valo_api.responses.competitive_updates_raw import CompetitiveMatchRaw
from valo_api.utils.dict_struct import DictStruct


class SeasonInfoRaw(DictStruct):
    SeasonID: str
    NumberOfWins: int
    NumberOfWinsWithPlacements: int
    NumberOfGames: int
    Rank: int
    CapstoneWins: int
    LeaderboardRank: int
    CompetitiveTier: int
    RankedRating: int
    GamesNeededForRating: int
    TotalWinsNeededForRank: int
    WinsByTier: Optional[Dict[str, int]] = None


class QueueSkill(DictStruct):
    TotalGamesNeededForRating: int
    TotalGamesNeededForLeaderboard: int
    CurrentSeasonGamesNeededForRating: int
    SeasonalInfoBySeasonID: Optional[Dict[str, SeasonInfoRaw]]


class QueueSkills(DictStruct):
    competitive: Optional[QueueSkill] = None
    custom: Optional[QueueSkill] = None
    deathmatch: Optional[QueueSkill] = None
    onefa: Optional[QueueSkill] = None
    seeding: Optional[QueueSkill] = None
    spikerush: Optional[QueueSkill] = None
    unrated: Optional[QueueSkill] = None


class MMRRawV1(DictStruct):
    Version: int
    Subject: str
    NewPlayerExperienceFinished: bool
    QueueSkills: QueueSkills
    LatestCompetitiveUpdate: Optional[CompetitiveMatchRaw]
    IsLeaderboardAnonymized: bool
    IsActRankBadgeHidden: bool
