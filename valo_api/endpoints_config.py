class EndpointsConfig:
    RAW = "/valorant/{version}/raw"
    CONTENT = "/valorant/{version}/content"
    STORE_FEATURED = "/valorant/{version}/store-featured"
    STORE_OFFERS = "/valorant/{version}/store-offers"
    STATUS = "/valorant/{version}/status/{region}"
    VERSION_INFO = "/valorant/{version}/version/{region}"
    WEBSITE = "/valorant/{version}/website/{countrycode}"
    LEADERBOARD = "/valorant/{version}/leaderboard/{region}"
    ACCOUNT_BY_NAME = "/valorant/{version}/account/{name}/{tag}"
    ACCOUNT_BY_PUUID = "/valorant/{version}/by-puuid/account/{puuid}"
    MATCH_DETAILS = "/valorant/{version}/match/{match_id}"

    MMR_DETAILS_BY_PUUID = "/valorant/{version}/by-puuid/mmr/{region}/{puuid}"
    MMR_DETAILS_BY_NAME = "/valorant/{version}/mmr/{region}/{name}/{tag}"

    MMR_HISTORY_BY_PUUID = "/valorant/{version}/by-puuid/mmr-history/{region}/{puuid}"
    MMR_HISTORY_BY_NAME = "/valorant/{version}/mmr-history/{region}/{name}/{tag}"

    MATCH_HISTORY_BY_PUUID = "/valorant/{version}/by-puuid/matches/{region}/{puuid}"
    MATCH_HISTORY_BY_NAME = "/valorant/{version}/matches/{region}/{name}/{tag}"

    CROSSHAIR = "/valorant/{version}/crosshair/generate"
