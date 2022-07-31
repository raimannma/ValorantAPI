from typing import List, Optional

from dataclasses import dataclass

from valo_api.utils.init_options import InitOptions


@dataclass
class MatchMetadataV3(InitOptions):
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


@dataclass
class MatchPlayerSessionPlaytimeV3(InitOptions):
    minutes: Optional[int] = None
    seconds: Optional[int] = None
    milliseconds: Optional[int] = None


@dataclass
class MatchFriendlyFireV3(InitOptions):
    incoming: int
    outgoing: int


@dataclass
class MatchPlayerBehaviorV3(InitOptions):
    afk_rounds: int
    friendly_fire: MatchFriendlyFireV3
    rounds_in_spawn: int

    def __post_init__(self):
        self.friendly_fire = MatchFriendlyFireV3.from_dict(**self.friendly_fire)


@dataclass
class MatchPlayerOSV3(InitOptions):
    name: str
    version: str


@dataclass
class MatchPlayerPlatformV3(InitOptions):
    type: str
    os: MatchPlayerOSV3

    def __post_init__(self):
        self.os = MatchPlayerOSV3.from_dict(**self.os)


@dataclass
class MatchPlayerAbilityCastsV3(InitOptions):
    c_cast: int
    q_cast: int
    e_cast: int
    x_cast: int


@dataclass
class MatchPlayerAbilityCasts2V3(InitOptions):
    c_casts: int
    q_casts: int
    e_cast: int
    x_cast: int


@dataclass
class MatchPlayerAssetsCardV3(InitOptions):
    small: str
    large: str
    wide: str


@dataclass
class MatchPlayerAssetsAgentV3(InitOptions):
    small: str
    bust: str
    full: str
    killfeed: str


@dataclass
class MatchPlayerAssetsV3(InitOptions):
    card: MatchPlayerAssetsCardV3
    agent: MatchPlayerAssetsAgentV3

    def __post_init__(self):
        self.card = MatchPlayerAssetsCardV3.from_dict(**self.card)
        self.agent = MatchPlayerAssetsAgentV3.from_dict(**self.agent)


@dataclass
class MatchPlayerStatsV3(InitOptions):
    score: int
    kills: int
    deaths: int
    assists: int
    bodyshots: int
    headshots: int
    legshots: int


@dataclass
class MatchPlayerEconomyReportV3(InitOptions):
    overall: int
    average: int


@dataclass
class MatchPlayerEconomyV3(InitOptions):
    spent: MatchPlayerEconomyReportV3
    loadout_value: MatchPlayerEconomyReportV3

    def __post_init__(self):
        self.spent = MatchPlayerEconomyReportV3.from_dict(**self.spent)
        self.loadout_value = MatchPlayerEconomyReportV3.from_dict(**self.loadout_value)


@dataclass
class MatchPlayerV3(InitOptions):
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

    def __post_init__(self):
        self.session_playtime = MatchPlayerSessionPlaytimeV3.from_dict(
            **self.session_playtime
        )
        self.behavior = MatchPlayerBehaviorV3.from_dict(**self.behavior)
        self.platform = MatchPlayerPlatformV3.from_dict(**self.platform)
        self.ability_casts = MatchPlayerAbilityCastsV3.from_dict(**self.ability_casts)
        self.assets = MatchPlayerAssetsV3.from_dict(**self.assets)
        self.stats = MatchPlayerStatsV3.from_dict(**self.stats)
        self.economy = MatchPlayerEconomyV3.from_dict(**self.economy)


@dataclass
class MatchPlayersV3(InitOptions):
    all_players: List[MatchPlayerV3]
    red: List[MatchPlayerV3]
    blue: List[MatchPlayerV3]

    def __post_init__(self):
        self.all_players = [
            MatchPlayerV3.from_dict(**player) for player in self.all_players
        ]
        self.red = [MatchPlayerV3.from_dict(**player) for player in self.red]
        self.blue = [MatchPlayerV3.from_dict(**player) for player in self.blue]


@dataclass
class MatchTeamV3(InitOptions):
    has_won: bool
    rounds_won: int
    rounds_lost: int


@dataclass
class MatchTeamsV3(InitOptions):
    red: MatchTeamV3
    blue: MatchTeamV3

    def __post_init__(self):
        self.red = MatchTeamV3.from_dict(**self.red)
        self.blue = MatchTeamV3.from_dict(**self.blue)


@dataclass
class Location(InitOptions):
    x: int
    y: int


@dataclass
class MatchRoundPlanterV3(InitOptions):
    puuid: str
    display_name: str
    team: str


@dataclass
class MatchRoundPlayerLocationV3(InitOptions):
    player_puuid: str
    player_display_name: str
    player_team: str
    location: Location
    view_radians: float

    def __post_init__(self):
        self.location = Location.from_dict(**self.location)


@dataclass
class MatchRoundPlantEventV3(InitOptions):
    plant_location: Location
    planted_by: MatchRoundPlanterV3
    plant_site: str
    plant_time_in_round: int
    player_locations_on_plant: List[MatchRoundPlayerLocationV3]

    def __post_init__(self):
        self.plant_location = (
            Location.from_dict(**self.plant_location) if self.plant_location else None
        )
        self.planted_by = (
            MatchRoundPlanterV3.from_dict(**self.planted_by)
            if self.planted_by
            else None
        )
        self.player_locations_on_plant = (
            [
                MatchRoundPlayerLocationV3.from_dict(**player)
                for player in self.player_locations_on_plant
            ]
            if self.player_locations_on_plant
            else None
        )


@dataclass
class MatchRoundDefuseEventV3(InitOptions):
    defuse_location: Location
    defused_by: MatchRoundPlanterV3
    defuse_time_in_round: int
    player_locations_on_defuse: List[MatchRoundPlayerLocationV3]

    def __post_init__(self):
        self.defuse_location = (
            Location.from_dict(**self.defuse_location) if self.defuse_location else None
        )
        self.defused_by = (
            MatchRoundPlanterV3.from_dict(**self.defused_by)
            if self.defused_by
            else None
        )
        self.player_locations_on_defuse = (
            [
                MatchRoundPlayerLocationV3.from_dict(**player)
                for player in self.player_locations_on_defuse
            ]
            if self.player_locations_on_defuse
            else None
        )


@dataclass
class MatchRoundDamageEventV3(InitOptions):
    receiver_puuid: str
    receiver_display_name: str
    receiver_team: str
    bodyshots: int
    damage: int
    headshots: int
    legshots: int


@dataclass
class WeaponAssets(InitOptions):
    display_icon: Optional[str] = None
    killfeed_icon: Optional[str] = None


@dataclass
class MatchRoundAssistantV3(InitOptions):
    assistant_puuid: str
    assistant_display_name: str
    assistant_team: str


@dataclass
class MatchRoundKillEventV3(InitOptions):
    kill_time_in_round: int
    kill_time_in_match: int
    killer_puuid: str
    killer_display_name: str
    killer_team: str
    victim_puuid: str
    victim_display_name: str
    victim_team: str
    victim_death_location: Location
    damage_weapon_id: int
    damage_weapon_assets: WeaponAssets
    secondary_fire_mode: bool
    player_locations_on_kill: List[MatchRoundPlayerLocationV3]
    assistants: List[MatchRoundAssistantV3]
    damage_weapon_name: Optional[str] = None

    def __post_init__(self):
        self.victim_death_location = Location.from_dict(**self.victim_death_location)
        self.damage_weapon_assets = WeaponAssets.from_dict(**self.damage_weapon_assets)
        self.player_locations_on_kill = [
            MatchRoundPlayerLocationV3.from_dict(**player)
            for player in self.player_locations_on_kill
        ]
        self.assistants = [
            MatchRoundAssistantV3.from_dict(**assistant)
            for assistant in self.assistants
        ]


@dataclass
class Weapon(InitOptions):
    id: str
    name: str
    assets: WeaponAssets

    def __post_init__(self):
        self.assets = WeaponAssets.from_dict(**self.assets)


@dataclass
class Armor(InitOptions):
    id: str
    name: str
    assets: WeaponAssets

    def __post_init__(self):
        self.assets = WeaponAssets.from_dict(**self.assets)


@dataclass
class MatchPlayerEconomyFullV3(InitOptions):
    loadout_value: int
    weapon: Weapon
    armor: Armor
    remaining: int
    spent: int

    def __post_init__(self):
        self.weapon = Weapon.from_dict(**self.weapon)
        self.armor = Armor.from_dict(**self.armor)


@dataclass
class MatchRoundPlayerStatsV3(InitOptions):
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

    def __post_init__(self):
        self.ability_casts = MatchPlayerAbilityCasts2V3.from_dict(**self.ability_casts)
        self.damage_events = [
            MatchRoundDamageEventV3.from_dict(**damage) for damage in self.damage_events
        ]
        self.kill_events = [
            MatchRoundKillEventV3.from_dict(**kill) for kill in self.kill_events
        ]
        self.economy = MatchPlayerEconomyFullV3.from_dict(**self.economy)


@dataclass
class MatchRoundV3(InitOptions):
    winning_team: str
    end_type: str
    bomb_planted: bool
    bomb_defused: bool
    plant_events: MatchRoundPlantEventV3
    defuse_events: MatchRoundDefuseEventV3
    player_stats: List[MatchRoundPlayerStatsV3]

    def __post_init__(self):
        self.plant_events = MatchRoundPlantEventV3.from_dict(**self.plant_events)
        self.defuse_events = MatchRoundDefuseEventV3.from_dict(**self.defuse_events)
        self.player_stats = [
            MatchRoundPlayerStatsV3.from_dict(**player) for player in self.player_stats
        ]


@dataclass
class MatchHistoryPointV3(InitOptions):
    metadata: MatchMetadataV3
    players: MatchPlayersV3
    teams: MatchTeamsV3
    rounds: List[MatchRoundV3]
    kills: List[MatchRoundKillEventV3]

    def __post_init__(self):
        self.metadata = MatchMetadataV3.from_dict(**self.metadata)
        self.players = MatchPlayersV3.from_dict(**self.players)
        self.teams = MatchTeamsV3.from_dict(**self.teams)
        self.rounds = [MatchRoundV3.from_dict(**round) for round in self.rounds]
        self.kills = [MatchRoundKillEventV3.from_dict(**kill) for kill in self.kills]
