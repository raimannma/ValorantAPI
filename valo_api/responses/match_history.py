from typing import List, Optional

from valo_api.utils.dict_struct import DictStruct


class MatchMetadataV3(DictStruct):
    map: str
    game_version: str
    game_length: int
    game_start: int
    game_start_patched: str
    rounds_played: int
    mode: str
    season_id: str
    platform: str
    matchid: str
    region: str
    cluster: str
    queue: str


class MatchPlayerSessionPlaytimeV3(DictStruct):
    minutes: Optional[int] = None
    seconds: Optional[int] = None
    milliseconds: Optional[int] = None


class MatchFriendlyFireV3(DictStruct):
    incoming: Optional[int] = None
    outgoing: Optional[int] = None


class MatchPlayerBehaviorV3(DictStruct):
    afk_rounds: float
    friendly_fire: MatchFriendlyFireV3
    rounds_in_spawn: Optional[float] = None


class MatchPlayerOSV3(DictStruct):
    name: str
    version: str


class MatchPlayerPlatformV3(DictStruct):
    type: str
    os: MatchPlayerOSV3


class MatchPlayerAbilityCastsV3(DictStruct):
    c_cast: Optional[int] = None
    q_cast: Optional[int] = None
    e_cast: Optional[int] = None
    x_cast: Optional[int] = None


class MatchPlayerAbilityCasts2V3(DictStruct):
    c_casts: Optional[int] = None
    q_casts: Optional[int] = None
    e_cast: Optional[int] = None
    x_cast: Optional[int] = None


class MatchPlayerAssetsCardV3(DictStruct):
    small: str
    large: str
    wide: str


class MatchPlayerAssetsAgentV3(DictStruct):
    small: str
    bust: str
    full: str
    killfeed: str


class MatchPlayerAssetsV3(DictStruct):
    card: MatchPlayerAssetsCardV3
    agent: MatchPlayerAssetsAgentV3


class MatchPlayerStatsV3(DictStruct):
    score: int
    kills: int
    deaths: int
    assists: int
    bodyshots: Optional[int] = None
    headshots: Optional[int] = None
    legshots: Optional[int] = None


class MatchPlayerEconomyReportV3(DictStruct):
    overall: int
    average: int


class MatchPlayerEconomyV3(DictStruct):
    spent: MatchPlayerEconomyReportV3
    loadout_value: MatchPlayerEconomyReportV3


class MatchPlayerV3(DictStruct):
    puuid: str
    name: str
    tag: str
    team: str
    level: int
    character: str
    currenttier: int
    currenttier_patched: str
    player_card: str
    player_title: str
    party_id: str
    session_playtime: MatchPlayerSessionPlaytimeV3
    behavior: MatchPlayerBehaviorV3
    platform: MatchPlayerPlatformV3
    ability_casts: MatchPlayerAbilityCastsV3
    assets: MatchPlayerAssetsV3
    stats: MatchPlayerStatsV3
    economy: MatchPlayerEconomyV3


class MatchPlayersV3(DictStruct):
    all_players: List[MatchPlayerV3]
    red: List[MatchPlayerV3]
    blue: List[MatchPlayerV3]


class MatchTeamV3(DictStruct):
    has_won: Optional[bool] = None
    rounds_won: Optional[int] = None
    rounds_lost: Optional[int] = None


class MatchTeamsV3(DictStruct):
    red: MatchTeamV3
    blue: MatchTeamV3


class Location(DictStruct):
    x: int
    y: int


class MatchRoundPlanterV3(DictStruct):
    puuid: str
    display_name: str
    team: str


class MatchRoundPlayerLocationV3(DictStruct):
    player_puuid: str
    player_display_name: str
    player_team: str
    location: Location
    view_radians: float


class MatchRoundPlantEventV3(DictStruct):
    plant_location: Optional[Location] = None
    planted_by: Optional[MatchRoundPlanterV3] = None
    plant_site: Optional[str] = None
    plant_time_in_round: Optional[int] = None
    player_locations_on_plant: Optional[List[MatchRoundPlayerLocationV3]] = None


class MatchRoundDefuseEventV3(DictStruct):
    defuse_location: Optional[Location] = None
    defused_by: Optional[MatchRoundPlanterV3] = None
    defuse_time_in_round: Optional[int] = None
    player_locations_on_defuse: Optional[List[MatchRoundPlayerLocationV3]] = None


class MatchRoundDamageEventV3(DictStruct):
    receiver_puuid: str
    receiver_display_name: str
    receiver_team: str
    bodyshots: int
    damage: int
    headshots: int
    legshots: int


class WeaponAssets(DictStruct):
    display_icon: Optional[str] = None
    killfeed_icon: Optional[str] = None


class MatchRoundAssistantV3(DictStruct):
    assistant_puuid: str
    assistant_display_name: str
    assistant_team: str


class MatchRoundKillEventV3(DictStruct):
    kill_time_in_round: int
    kill_time_in_match: int
    killer_puuid: str
    killer_display_name: str
    killer_team: str
    victim_puuid: str
    victim_display_name: str
    victim_team: str
    victim_death_location: Location
    damage_weapon_id: str
    damage_weapon_assets: WeaponAssets
    secondary_fire_mode: bool
    player_locations_on_kill: List[MatchRoundPlayerLocationV3]
    assistants: List[MatchRoundAssistantV3]
    damage_weapon_name: Optional[str] = None


class Weapon(DictStruct):
    assets: WeaponAssets
    id: Optional[str] = None
    name: Optional[str] = None


class Armor(Weapon):
    pass


class MatchPlayerEconomyFullV3(DictStruct):
    loadout_value: int
    weapon: Weapon
    armor: Armor
    remaining: int
    spent: int


class MatchRoundPlayerStatsV3(DictStruct):
    ability_casts: MatchPlayerAbilityCasts2V3
    player_puuid: str
    player_display_name: str
    player_team: str
    damage_events: List[MatchRoundDamageEventV3]
    damage: int
    bodyshots: int
    headshots: int
    legshots: int
    kill_events: List[MatchRoundKillEventV3]
    kills: int
    score: int
    economy: MatchPlayerEconomyFullV3
    was_afk: bool
    was_penalized: bool
    stayed_in_spawn: bool


class MatchRoundV3(DictStruct):
    winning_team: str
    end_type: str
    bomb_planted: bool
    bomb_defused: bool
    plant_events: MatchRoundPlantEventV3
    defuse_events: MatchRoundDefuseEventV3
    player_stats: List[MatchRoundPlayerStatsV3]


class MatchHistoryPointV3(DictStruct):
    metadata: MatchMetadataV3
    players: MatchPlayersV3
    teams: MatchTeamsV3
    rounds: List[MatchRoundV3]
    kills: List[MatchRoundKillEventV3]
