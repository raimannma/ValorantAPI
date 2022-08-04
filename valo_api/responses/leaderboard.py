from typing import List, Optional

from dataclasses import dataclass

from valo_api.utils.init_options import InitOptions


@dataclass
class LeaderboardPlayerV1(InitOptions):
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


@dataclass
class LeaderboardPlayerV2(InitOptions):
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


@dataclass
class LeaderboardV2(InitOptions):
    total_players: int
    radiant_threshold: int
    immortal_3_threshold: int
    immortal_2_threshold: int
    immortal_1_threshold: int
    players: List[LeaderboardPlayerV2]
    last_update: Optional[int] = None
    next_update: Optional[int] = None

    def __post_init__(self):
        self.players = [
            LeaderboardPlayerV2(**player)
            for player in self.players
            if player is not None
        ]
