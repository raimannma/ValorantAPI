from typing import Dict, List, Union

from dataclasses import dataclass

from valo_api.utils.init_options import InitOptions


@dataclass
class MMRDetailsV1(InitOptions):
    name: str
    tag: str
    currenttier: int
    currenttierpatched: str
    ranking_in_tier: int
    mmr_change_to_last_game: int
    elo: int
    old: bool


@dataclass
class CurrentDataV2(InitOptions):
    currenttier: int
    currenttierpatched: str
    ranking_in_tier: int
    mmr_change_to_last_game: int
    elo: int
    games_needed_for_rating: int
    old: bool


@dataclass
class ActRankWinV2(InitOptions):
    patched_tier: str
    tier: int


@dataclass
class SeasonDataV2(InitOptions):
    wins: int
    number_of_games: int
    final_rank: int
    final_rank_patched: str
    act_rank_wins: List[ActRankWinV2]
    old: bool

    def __post_init__(self):
        self.act_rank_wins = [ActRankWinV2.from_dict(**x) for x in self.act_rank_wins]


@dataclass
class SeasonDataV2Error(InitOptions):
    error: str


@dataclass
class MMRDetailsV2(InitOptions):
    name: str
    tag: str
    current_data: CurrentDataV2
    by_season: Dict[str, Union[SeasonDataV2, SeasonDataV2Error]]

    def __post_init__(self):
        self.current_data = CurrentDataV2.from_dict(**self.current_data)
        self.by_season = {
            k: SeasonDataV2.from_dict(**v)
            if "error" not in v
            else SeasonDataV2Error.from_dict(**v)
            for k, v in self.by_season.items()
        }
