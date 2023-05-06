from typing import List, Optional

from valo_api.utils.dict_struct import DictStruct


class PremierLeaderboardCustomizationV1(DictStruct):
    icon: str
    image: str
    primary: str
    secondary: str
    tertiary: str


class PremierLeaderboardV1(DictStruct):
    id: str
    name: str
    tag: str
    conference: str
    division: int
    affinity: str
    region: str
    losses: int
    wins: int
    score: int
    ranking: int
    customization: PremierLeaderboardCustomizationV1
