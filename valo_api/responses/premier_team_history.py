from typing import List, Optional

from valo_api.responses.premier_leaderboard import PremierLeaderboardCustomizationV1
from valo_api.utils.dict_struct import DictStruct


class PremierTeamHistoryLeagueMatchesV1(DictStruct):
    id: str
    points_before: int
    points_after: int
    started_at: str


class PremierTeamHistoryTournamentMatchesV1(DictStruct):
    tournament_id: str
    placement: int
    placement_league_bonus: int
    points_before: int
    points_after: int
    matches: List[str]


class PremierTeamHistoryV1(DictStruct):
    league_matches: List[PremierTeamHistoryLeagueMatchesV1]
    tournament_matches: List[PremierTeamHistoryTournamentMatchesV1]
