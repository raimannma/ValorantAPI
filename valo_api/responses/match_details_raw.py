from typing import Dict, List, Optional

from msgspec import Struct

from valo_api.responses.match_history import Location


class MatchInfoRaw(Struct):
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
    partyRRPenalties: Dict[str, float]
    shouldMatchDisablePenalties: Optional[bool] = None


class PlayerPlatformInfoRaw(Struct):
    platformType: str
    platformOS: str
    platformOSVersion: str
    platformChipset: str


class PlayerAbilityCastsRaw(Struct):
    grenadeCasts: int
    ability1Casts: int
    ability2Casts: int
    ultimateCasts: int


class PlayerStatsRaw(Struct):
    score: int
    roundsPlayed: int
    kills: int
    deaths: int
    assists: int
    playtimeMillis: int
    abilityCasts: Optional[PlayerAbilityCastsRaw] = None


class PlayerRoundDamageRaw(Struct):
    round: int
    receiver: str
    damage: int


class PlayerBehaviorFactorsRaw(Struct):
    afkRounds: float
    damageParticipationOutgoing: Optional[int] = None
    friendlyFireIncoming: Optional[int] = None
    friendlyFireOutgoing: Optional[float] = None
    stayedInSpawnRounds: Optional[float] = None


class PlayerBasicMovementRaw(Struct):
    idleTimeMillis: int
    objectiveCompleteTimeMillis: int


class PlayerBasicGunSkillRaw(Struct):
    idleTimeMillis: int
    objectiveCompleteTimeMillis: int


class PlayerAdaptiveBotsRaw(Struct):
    idleTimeMillis: int
    objectiveCompleteTimeMillis: int
    adaptiveBotAverageDurationMillisAllAttempts: int
    adaptiveBotAverageDurationMillisFirstAttempt: int
    killDetailsFirstAttempt: Optional[dict]


class PlayerAbilityRaw(Struct):
    idleTimeMillis: int
    objectiveCompleteTimeMillis: int


class PlayerBombPlantRaw(Struct):
    idleTimeMillis: int
    objectiveCompleteTimeMillis: int


class PlayerDefendBombSiteRaw(Struct):
    idleTimeMillis: int
    objectiveCompleteTimeMillis: int
    success: bool


class PlayerSettingStatusRaw(Struct):
    isMouseSensitivityDefault: bool
    isCrosshairDefault: bool


class PlayerExperienceDetailsRaw(Struct):
    basicMovement: PlayerBasicMovementRaw
    basicGunSkill: PlayerBasicGunSkillRaw
    adaptiveBots: PlayerAdaptiveBotsRaw
    ability: PlayerAbilityRaw
    bombPlant: PlayerBombPlantRaw
    defendBombSite: PlayerDefendBombSiteRaw
    settingStatus: PlayerSettingStatusRaw


class MatchPlayersRaw(Struct):
    subject: str
    gameName: str
    tagLine: str
    platformInfo: PlayerPlatformInfoRaw
    teamId: str
    partyId: str
    characterId: str
    stats: PlayerStatsRaw
    competitiveTier: int
    playerCard: str
    playerTitle: str
    accountLevel: int
    behaviorFactors: PlayerBehaviorFactorsRaw
    newPlayerExperienceDetails: PlayerExperienceDetailsRaw
    roundDamage: Optional[List[PlayerRoundDamageRaw]] = None
    sessionPlaytimeMinutes: Optional[int] = None


class MatchTeamRaw(Struct):
    teamId: str
    won: bool
    roundsPlayed: int
    numPoints: int


class PlayerLocationsRaw(Struct):
    subject: str
    viewRadians: float
    location: Location


class KillFinishingDamageRaw(Struct):
    damageType: str
    damageItem: str
    isSecondaryFireMode: bool


class PlayerKillsRaw(Struct):
    gameTime: int
    roundTime: int
    killer: str
    victim: str
    victimLocation: Location
    assistants: List[str]
    playerLocations: List[PlayerLocationsRaw]
    finishingDamage: KillFinishingDamageRaw


class PlayerDamageRaw(Struct):
    receiver: str
    damage: int
    legshots: int
    bodyshots: int
    headshots: int


class PlayerEconomyRaw(Struct):
    loadoutValue: int
    weapon: str
    armor: str
    remaining: int
    spent: int
    subject: Optional[str] = None


class PlayerAbilityEffectsRaw(Struct):
    grenadeEffects: Optional[dict]
    ability1Effects: Optional[dict]
    ability2Effects: Optional[dict]
    ultimateEffects: Optional[dict]


class RoundPlayerStatsRaw(Struct):
    subject: str
    kills: List[PlayerKillsRaw]
    damage: List[PlayerDamageRaw]
    score: int
    economy: PlayerEconomyRaw
    ability: PlayerAbilityEffectsRaw
    wasAfk: bool
    wasPenalized: bool
    stayedInSpawn: bool


class PlayerScoreRaw(Struct):
    subject: str
    score: int


class MatchRoundResultsRaw(Struct):
    roundNum: int
    roundResult: str
    roundCeremony: str
    winningTeam: str
    plantRoundTime: int
    plantLocation: Location
    plantSite: str
    defuseRoundTime: int
    defuseLocation: Location
    playerStats: List[RoundPlayerStatsRaw]
    roundResultCode: str
    playerEconomies: Optional[List[PlayerEconomyRaw]] = None
    playerScores: Optional[List[PlayerScoreRaw]] = None
    plantPlayerLocations: Optional[List[PlayerLocationsRaw]] = None
    defusePlayerLocations: Optional[List[PlayerLocationsRaw]] = None


class MatchDetailsRawV1(Struct):
    matchInfo: MatchInfoRaw
    players: List[MatchPlayersRaw]
    bots: List[dict]
    coaches: List[dict]
    teams: List[MatchTeamRaw]
    roundResults: Optional[List[MatchRoundResultsRaw]]
    kills: List[PlayerKillsRaw]
