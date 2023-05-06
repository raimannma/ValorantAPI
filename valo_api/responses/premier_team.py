from typing import List, Optional

from valo_api.responses.premier_leaderboard import PremierLeaderboardCustomizationV1
from valo_api.utils.dict_struct import DictStruct


class PremierTeamStatsV1(DictStruct):
    wins: int
    matches: int
    losses: int


class PremierTeamPlacementV1(DictStruct):
    points: int
    conference: str
    division: int


class PremierTeamMemberV1(DictStruct):
    puuid: str
    name: str
    tag: str


class PremierTeamV1(DictStruct):
    id: str
    name: str
    tag: str
    enrolled: bool
    stats: Optional[PremierTeamStatsV1] = None
    placement: Optional[PremierTeamPlacementV1] = None
    customization: Optional[PremierLeaderboardCustomizationV1] = None
    member: Optional[List[PremierTeamMemberV1]] = None
