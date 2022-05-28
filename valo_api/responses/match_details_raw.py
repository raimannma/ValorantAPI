from typing import Dict, List, Optional

from dataclasses import dataclass

from valo_api.responses.match_history import Location
from valo_api.utils.init_options import InitOptions


@dataclass
class MatchInfoRaw(InitOptions):
    matchId: str
    mapId: str
    gamePodId: str
    gameLoopZone: str
    gameServerAddress: str
    gameVersion: str
    gameLengthMillis: int
    gameStartMillis: int
    provisioningFlowID: str
    isCompleted: bool
    customGameName: str
    forcePostProcessing: bool
    queueID: str
    gameMode: str
    isRanked: bool
    isMatchSampled: bool
    seasonId: str
    completionState: str
    platformType: str
    partyRRPenalties: Dict[str, int]
    shouldMatchDisablePenalties: bool


@dataclass
class PlayerPlatformInfoRaw(InitOptions):
    platformType: str
    platformOS: str
    platformOSVersion: str
    platformChipset: str


@dataclass
class PlayerAbilityCastsRaw(InitOptions):
    grenadeCasts: int
    ability1Casts: int
    ability2Casts: int
    ultimateCasts: int


@dataclass
class PlayerStatsRaw(InitOptions):
    score: int
    roundsPlayed: int
    kills: int
    deaths: int
    assists: int
    playtimeMillis: int
    abilityCasts: PlayerAbilityCastsRaw

    def __post_init__(self):
        self.abilityCasts = PlayerAbilityCastsRaw.from_dict(**self.abilityCasts)


@dataclass
class PlayerRoundDamageRaw(InitOptions):
    round: int
    receiver: str
    damage: int


@dataclass
class PlayerBehaviorFactorsRaw(InitOptions):
    afkRounds: int
    damageParticipationOutgoing: int
    friendlyFireIncoming: int
    friendlyFireOutgoing: int
    stayedInSpawnRounds: float


@dataclass
class PlayerBasicMovementRaw(InitOptions):
    idleTimeMillis: int
    objectiveCompleteTimeMillis: int


@dataclass
class PlayerBasicGunSkillRaw(InitOptions):
    idleTimeMillis: int
    objectiveCompleteTimeMillis: int


@dataclass
class PlayerAdaptiveBotsRaw(InitOptions):
    idleTimeMillis: int
    objectiveCompleteTimeMillis: int
    adaptiveBotAverageDurationMillisAllAttempts: int
    adaptiveBotAverageDurationMillisFirstAttempt: int
    killDetailsFirstAttempt: Optional[dict]


@dataclass
class PlayerAbilityRaw(InitOptions):
    idleTimeMillis: int
    objectiveCompleteTimeMillis: int


@dataclass
class PlayerBombPlantRaw(InitOptions):
    idleTimeMillis: int
    objectiveCompleteTimeMillis: int


@dataclass
class PlayerDefendBombSiteRaw(InitOptions):
    idleTimeMillis: int
    objectiveCompleteTimeMillis: int
    success: bool


@dataclass
class PlayerSettingStatusRaw(InitOptions):
    isMouseSensitivityDefault: bool
    isCrosshairDefault: bool


@dataclass
class PlayerExperienceDetailsRaw(InitOptions):
    basicMovement: PlayerBasicMovementRaw
    basicGunSkill: PlayerBasicGunSkillRaw
    adaptiveBots: PlayerAdaptiveBotsRaw
    ability: PlayerAbilityRaw
    bombPlant: PlayerBombPlantRaw
    defendBombSite: PlayerDefendBombSiteRaw
    settingStatus: PlayerSettingStatusRaw

    def __post_init__(self):
        self.basicMovement = PlayerBasicMovementRaw.from_dict(**self.basicMovement)
        self.basicGunSkill = PlayerBasicGunSkillRaw.from_dict(**self.basicGunSkill)
        self.adaptiveBots = PlayerAdaptiveBotsRaw.from_dict(**self.adaptiveBots)
        self.ability = PlayerAbilityRaw.from_dict(**self.ability)
        self.bombPlant = PlayerBombPlantRaw.from_dict(**self.bombPlant)
        self.defendBombSite = PlayerDefendBombSiteRaw.from_dict(**self.defendBombSite)
        self.settingStatus = PlayerSettingStatusRaw.from_dict(**self.settingStatus)


@dataclass
class MatchPlayersRaw(InitOptions):
    subject: str
    gameName: str
    tagLine: str
    platformInfo: PlayerPlatformInfoRaw
    teamId: str
    partyId: str
    characterId: str
    stats: PlayerStatsRaw
    roundDamage: List[PlayerRoundDamageRaw]
    competitiveTier: int
    playerCard: str
    playerTitle: str
    accountLevel: int
    sessionPlaytimeMinutes: int
    behaviorFactors: PlayerBehaviorFactorsRaw
    newPlayerExperienceDetails: PlayerExperienceDetailsRaw

    def __post_init__(self):
        self.platformInfo = PlayerPlatformInfoRaw.from_dict(**self.platformInfo)
        self.stats = PlayerStatsRaw.from_dict(**self.stats)
        self.roundDamage = [
            PlayerRoundDamageRaw.from_dict(**x) for x in self.roundDamage
        ]
        self.behaviorFactors = PlayerBehaviorFactorsRaw.from_dict(
            **self.behaviorFactors
        )
        self.newPlayerExperienceDetails = PlayerExperienceDetailsRaw.from_dict(
            **self.newPlayerExperienceDetails
        )


@dataclass
class MatchTeamRaw(InitOptions):
    teamId: str
    won: bool
    roundsPlayed: int
    numPoints: int


@dataclass
class PlayerLocationsRaw(InitOptions):
    subject: str
    viewRadians: float
    location: Location

    def __post_init__(self):
        self.location = Location.from_dict(**self.location)


@dataclass
class KillFinishingDamageRaw(InitOptions):
    damageType: str
    damageItem: str
    isSecondaryFireMode: bool


@dataclass
class PlayerKillsRaw(InitOptions):
    gameTime: int
    roundTime: int
    killer: str
    victim: str
    victimLocation: Location
    assistants: List[str]
    playerLocations: List[PlayerLocationsRaw]
    finishingDamage: KillFinishingDamageRaw

    def __post_init__(self):
        self.victimLocation = Location.from_dict(**self.victimLocation)
        self.playerLocations = [
            PlayerLocationsRaw.from_dict(**x) for x in self.playerLocations
        ]
        self.finishingDamage = KillFinishingDamageRaw.from_dict(**self.finishingDamage)


@dataclass
class PlayerDamageRaw(InitOptions):
    receiver: str
    damage: int
    legshots: int
    bodyshots: int
    headshots: int


@dataclass
class PlayerEconomyRaw(InitOptions):
    loadoutValue: int
    weapon: str
    armor: str
    remaining: int
    spent: int
    subject: Optional[str] = None


@dataclass
class PlayerAbilityEffectsRaw(InitOptions):
    grenadeEffects: Optional[dict]
    ability1Effects: Optional[dict]
    ability2Effects: Optional[dict]
    ultimateEffects: Optional[dict]


@dataclass
class RoundPlayerStatsRaw(InitOptions):
    subject: str
    kills: List[PlayerKillsRaw]
    damage: List[PlayerDamageRaw]
    score: int
    economy: PlayerEconomyRaw
    ability: PlayerAbilityEffectsRaw
    wasAfk: bool
    wasPenalized: bool
    stayedInSpawn: bool

    def __post_init__(self):
        self.kills = [PlayerKillsRaw.from_dict(**x) for x in self.kills]
        self.damage = [PlayerDamageRaw.from_dict(**x) for x in self.damage]
        self.economy = PlayerEconomyRaw.from_dict(**self.economy)
        self.ability = PlayerAbilityEffectsRaw.from_dict(**self.ability)


@dataclass
class PlayerScoreRaw(InitOptions):
    subject: str
    score: int


@dataclass
class MatchRoundResultsRaw(InitOptions):
    roundNum: int
    roundResult: str
    roundCeremony: str
    winningTeam: str
    plantRoundTime: int
    plantPlayerLocations: List[PlayerLocationsRaw]
    plantLocation: Location
    plantSite: str
    defuseRoundTime: int
    defusePlayerLocations: List[PlayerLocationsRaw]
    defuseLocation: Location
    playerStats: List[RoundPlayerStatsRaw]
    roundResultCode: str
    playerEconomies: List[PlayerEconomyRaw]
    playerScores: List[PlayerScoreRaw]

    def __post_init__(self):
        self.plantPlayerLocations = [
            PlayerLocationsRaw.from_dict(**x) for x in self.plantPlayerLocations or []
        ]
        self.plantLocation = Location.from_dict(**self.plantLocation)
        self.defusePlayerLocations = [
            PlayerLocationsRaw.from_dict(**x) for x in self.defusePlayerLocations or []
        ]
        self.defuseLocation = Location.from_dict(**self.defuseLocation)
        self.playerStats = [
            RoundPlayerStatsRaw.from_dict(**x) for x in self.playerStats
        ]
        self.playerEconomies = [
            PlayerEconomyRaw.from_dict(**x) for x in self.playerEconomies
        ]
        self.playerScores = [PlayerScoreRaw.from_dict(**x) for x in self.playerScores]


@dataclass
class MatchDetailsRawV1(InitOptions):
    matchInfo: MatchInfoRaw
    players: List[MatchPlayersRaw]
    bots: List[dict]
    coaches: List[dict]
    teams: List[MatchTeamRaw]
    roundResults: List[MatchRoundResultsRaw]
    kills: List[PlayerKillsRaw]

    def __post_init__(self):
        self.matchInfo = MatchInfoRaw.from_dict(**self.matchInfo)
        self.players = [MatchPlayersRaw.from_dict(**p) for p in self.players]
        self.teams = [MatchTeamRaw.from_dict(**t) for t in self.teams]
        self.roundResults = [
            MatchRoundResultsRaw.from_dict(**r) for r in self.roundResults
        ]
        self.kills = [PlayerKillsRaw.from_dict(**k) for k in self.kills]
