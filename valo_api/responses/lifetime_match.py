from typing import Optional

from valo_api.utils.dict_struct import DictStruct


class LifetimeMatchMapV1(DictStruct):
    id: str
    name: str


class LifetimeMatchSeasonV1(DictStruct):
    id: str
    short: str


class LifetimeMatchMetaV1(DictStruct):
    map: LifetimeMatchMapV1
    version: str
    started_at: str
    season: LifetimeMatchSeasonV1
    cluster: str
    region: Optional[str] = None
    mode: Optional[str] = None


class LifetimeMatchCharacterV1(DictStruct):
    id: str
    name: str


class LifetimeMatchShotsV1(DictStruct):
    head: int
    body: int
    leg: int


class LifetimeMatchDamageV1(DictStruct):
    made: int
    received: int


class LifetimeMatchStatsV1(DictStruct):
    puuid: str
    team: str
    level: int
    character: LifetimeMatchCharacterV1
    tier: int
    score: int
    kills: int
    deaths: int
    assists: int
    shots: LifetimeMatchShotsV1
    damage: LifetimeMatchDamageV1


class LifetimeMatchTeamsV1(DictStruct):
    blue: Optional[int] = None
    red: Optional[int] = None


class LifetimeMatchV1(DictStruct):
    meta: LifetimeMatchMetaV1
    stats: LifetimeMatchStatsV1
    teams: LifetimeMatchTeamsV1
