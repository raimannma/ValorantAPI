from typing import Dict, List, Optional

from valo_api.responses.match_history import Location
from valo_api.utils.dict_struct import DictStruct


class MatchInfoRaw(DictStruct):
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


class PlayerPlatformInfoRaw(DictStruct):
    platformType: str
    platformOS: str
    platformOSVersion: str
    platformChipset: str


class PlayerAbilityCastsRaw(DictStruct):
    grenadeCasts: int
    ability1Casts: int
    ability2Casts: int
    ultimateCasts: int


class PlayerStatsRaw(DictStruct):
    score: int
    roundsPlayed: int
    kills: int
    deaths: int
    assists: int
    playtimeMillis: int
    abilityCasts: Optional[PlayerAbilityCastsRaw] = None


class PlayerRoundDamageRaw(DictStruct):
    round: int
    receiver: str
    damage: int


class PlayerBehaviorFactorsRaw(DictStruct):
    afkRounds: float
    damageParticipationOutgoing: Optional[int] = None
    friendlyFireIncoming: Optional[int] = None
    friendlyFireOutgoing: Optional[float] = None
    stayedInSpawnRounds: Optional[float] = None


class PlayerBasicMovementRaw(DictStruct):
    idleTimeMillis: int
    objectiveCompleteTimeMillis: int


class PlayerBasicGunSkillRaw(DictStruct):
    idleTimeMillis: int
    objectiveCompleteTimeMillis: int


class PlayerAdaptiveBotsRaw(DictStruct):
    idleTimeMillis: int
    objectiveCompleteTimeMillis: int
    adaptiveBotAverageDurationMillisAllAttempts: int
    adaptiveBotAverageDurationMillisFirstAttempt: int
    killDetailsFirstAttempt: Optional[dict]


class PlayerAbilityRaw(DictStruct):
    idleTimeMillis: int
    objectiveCompleteTimeMillis: int


class PlayerBombPlantRaw(DictStruct):
    idleTimeMillis: int
    objectiveCompleteTimeMillis: int


class PlayerDefendBombSiteRaw(DictStruct):
    idleTimeMillis: int
    objectiveCompleteTimeMillis: int
    success: bool


class PlayerSettingStatusRaw(DictStruct):
    isMouseSensitivityDefault: bool
    isCrosshairDefault: bool


class PlayerExperienceDetailsRaw(DictStruct):
    basicMovement: PlayerBasicMovementRaw
    basicGunSkill: PlayerBasicGunSkillRaw
    adaptiveBots: PlayerAdaptiveBotsRaw
    ability: PlayerAbilityRaw
    bombPlant: PlayerBombPlantRaw
    defendBombSite: PlayerDefendBombSiteRaw
    settingStatus: PlayerSettingStatusRaw


class MatchPlayersRaw(DictStruct):
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


class MatchTeamRaw(DictStruct):
    teamId: str
    won: bool
    roundsPlayed: int
    numPoints: int


class PlayerLocationsRaw(DictStruct):
    subject: str
    viewRadians: float
    location: Location


class KillFinishingDamageRaw(DictStruct):
    damageType: str
    damageItem: str
    isSecondaryFireMode: bool


class PlayerKillsRaw(DictStruct):
    gameTime: int
    roundTime: int
    killer: str
    victim: str
    victimLocation: Location
    assistants: List[str]
    playerLocations: List[PlayerLocationsRaw]
    finishingDamage: KillFinishingDamageRaw


class PlayerDamageRaw(DictStruct):
    receiver: str
    damage: int
    legshots: int
    bodyshots: int
    headshots: int


class PlayerEconomyRaw(DictStruct):
    loadoutValue: int
    weapon: str
    armor: str
    remaining: int
    spent: int
    subject: Optional[str] = None


class PlayerAbilityEffectsRaw(DictStruct):
    grenadeEffects: Optional[dict]
    ability1Effects: Optional[dict]
    ability2Effects: Optional[dict]
    ultimateEffects: Optional[dict]


class RoundPlayerStatsRaw(DictStruct):
    subject: str
    kills: List[PlayerKillsRaw]
    damage: List[PlayerDamageRaw]
    score: int
    economy: PlayerEconomyRaw
    ability: PlayerAbilityEffectsRaw
    wasAfk: bool
    wasPenalized: bool
    stayedInSpawn: bool


class PlayerScoreRaw(DictStruct):
    subject: str
    score: int


class MatchRoundResultsRaw(DictStruct):
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
    bombPlanter: Optional[str] = None
    bombDefuser: Optional[str] = None
    playerEconomies: Optional[List[PlayerEconomyRaw]] = None
    playerScores: Optional[List[PlayerScoreRaw]] = None
    plantPlayerLocations: Optional[List[PlayerLocationsRaw]] = None
    defusePlayerLocations: Optional[List[PlayerLocationsRaw]] = None


class MatchDetailsRawV1(DictStruct):
    matchInfo: MatchInfoRaw
    players: List[MatchPlayersRaw]
    bots: List[dict]
    coaches: List[dict]
    teams: List[MatchTeamRaw]
    roundResults: Optional[List[MatchRoundResultsRaw]]
    kills: List[PlayerKillsRaw]
