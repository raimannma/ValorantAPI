from typing import List, Optional, Union

from enum import Enum

from PIL import Image

from valo_api.endpoint import Endpoint
from valo_api.responses.account_details import AccountDetailsV1
from valo_api.responses.competitive_updates_raw import CompetitiveUpdatesRawV1
from valo_api.responses.content import ContentV1
from valo_api.responses.leaderboard import LeaderboardPlayerV1, LeaderboardV2
from valo_api.responses.lifetime_match import LifetimeMatchV1
from valo_api.responses.match_details_raw import MatchDetailsRawV1
from valo_api.responses.match_history import MatchHistoryPointV3
from valo_api.responses.match_history_raw import MatchHistoryRawV1
from valo_api.responses.mmr_details import MMRDetailsV2
from valo_api.responses.mmr_history import MMRHistoryPointV1
from valo_api.responses.mmr_raw import MMRRawV1
from valo_api.responses.status import StatusV1
from valo_api.responses.store_featured import BundleV2, StoreFeaturedV1
from valo_api.responses.store_offers import StoreOffersV2
from valo_api.responses.version_info import VersionInfoV1
from valo_api.responses.website import WebsiteBannerV1


class EndpointsConfig(Enum):
    RAW_MATCH_DETAILS = Endpoint(
        path="/valorant/{version}/raw",
        method="POST",
        f_name="get_raw_match_details_data",
        return_type=MatchDetailsRawV1,
        data_response=False,
        kwargs={
            "version": str,
            "value": Optional[str],
            "region": Optional[str],
            "queries": Optional[dict],
        },
        query_args={
            "type": "matchdetails",
            "value": "{value}",
            "region": "{region}",
            "queries": "{queries}",
        },
    )
    RAW_MATCH_HISTORY = Endpoint(
        path="/valorant/{version}/raw",
        method="POST",
        f_name="get_raw_match_history_data",
        return_type=MatchHistoryRawV1,
        data_response=False,
        kwargs={
            "version": str,
            "value": Optional[str],
            "region": Optional[str],
            "queries": Optional[dict],
        },
        query_args={
            "type": "matchhistory",
            "value": "{value}",
            "region": "{region}",
            "queries": "{queries}",
        },
    )
    RAW_MMR = Endpoint(
        path="/valorant/{version}/raw",
        method="POST",
        f_name="get_raw_mmr_data",
        return_type=MMRRawV1,
        data_response=False,
        kwargs={
            "version": str,
            "value": Optional[str],
            "region": Optional[str],
            "queries": Optional[dict],
        },
        query_args={
            "type": "mmr",
            "value": "{value}",
            "region": "{region}",
            "queries": "{queries}",
        },
    )
    RAW_COMPETITIVE_UPDATES = Endpoint(
        path="/valorant/{version}/raw",
        method="POST",
        f_name="get_raw_competitive_updates_data",
        return_type=CompetitiveUpdatesRawV1,
        data_response=False,
        kwargs={
            "version": str,
            "value": Optional[str],
            "region": Optional[str],
            "queries": Optional[dict],
        },
        query_args={
            "type": "competitiveupdates",
            "value": "{value}",
            "region": "{region}",
            "queries": "{queries}",
        },
    )
    CONTENT = Endpoint(
        path="/valorant/{version}/content",
        f_name="get_content",
        return_type=ContentV1,
        data_response=False,
        kwargs={
            "version": str,
            "locale": Optional[str],
        },
        query_args={
            "locale": "{locale}",
        },
    )
    STORE_FEATURED = Endpoint(
        path="/valorant/{version}/store-featured",
        f_name="get_store_featured",
        versions=["v1", "v2"],
        return_type=Union[StoreFeaturedV1, List[BundleV2]],
        kwargs={"version": str},
    )
    STORE_OFFERS = Endpoint(
        path="/valorant/{version}/store-offers",
        f_name="get_store_offers",
        versions=["v2"],
        return_type=StoreOffersV2,
        kwargs={"version": str},
    )
    STATUS = Endpoint(
        path="/valorant/{version}/status/{region}",
        f_name="get_status",
        return_type=StatusV1,
        kwargs={"version": str, "region": str},
    )
    VERSION_INFO = Endpoint(
        path="/valorant/{version}/version/{region}",
        f_name="get_version_info",
        return_type=VersionInfoV1,
        kwargs={"version": str, "region": str},
    )
    WEBSITE = Endpoint(
        path="/valorant/{version}/website/{countrycode}",
        f_name="get_website",
        return_type=List[WebsiteBannerV1],
        kwargs={"version": str, "countrycode": str},
    )
    LEADERBOARD = Endpoint(
        path="/valorant/{version}/leaderboard/{region}",
        f_name="get_leaderboard",
        versions=["v1", "v2"],
        return_type=Union[LeaderboardV2, List[LeaderboardPlayerV1]],
        data_response=False,
        kwargs={
            "version": str,
            "region": str,
            "puuid": Optional[str],
            "name": Optional[str],
            "tag": Optional[str],
            "season_id": Optional[str],
            "start": Optional[int],
        },
        query_args={
            "puuid": "{puuid}",
            "name": "{name}",
            "tag": "{tag}",
            "season_id": "{season_id}",
            "start": "{start}",
        },
    )
    ACCOUNT_BY_NAME = Endpoint(
        path="/valorant/{version}/account/{name}/{tag}",
        f_name="get_account_details_by_name",
        return_type=AccountDetailsV1,
        kwargs={"version": str, "name": str, "tag": str, "force_update": bool},
        query_args={"force": "{force_update}"},
    )
    ACCOUNT_BY_PUUID = Endpoint(
        path="/valorant/{version}/by-puuid/account/{puuid}",
        f_name="get_account_details_by_puuid",
        return_type=AccountDetailsV1,
        kwargs={"version": str, "puuid": str, "force_update": bool},
        query_args={"force": "{force_update}"},
    )
    MATCH_DETAILS = Endpoint(
        path="/valorant/{version}/match/{match_id}",
        f_name="get_match_details",
        versions=["v2"],
        return_type=MatchHistoryPointV3,
        kwargs={"version": str, "match_id": str},
    )
    MMR_DETAILS_BY_PUUID = Endpoint(
        path="/valorant/{version}/by-puuid/mmr/{region}/{puuid}",
        f_name="get_mmr_details_by_puuid",
        versions=["v1", "v2"],
        return_type=MMRDetailsV2,
        kwargs={"version": str, "region": str, "puuid": str, "filter": str},
        query_args={"filter": "{filter}"},
    )
    MMR_DETAILS_BY_NAME = Endpoint(
        path="/valorant/{version}/mmr/{region}/{name}/{tag}",
        f_name="get_mmr_details_by_name",
        versions=["v2"],
        return_type=MMRDetailsV2,
        kwargs={"version": str, "region": str, "name": str, "tag": str, "filter": str},
        query_args={"filter": "{filter}"},
    )
    MMR_HISTORY_BY_PUUID = Endpoint(
        path="/valorant/{version}/by-puuid/mmr-history/{region}/{puuid}",
        f_name="get_mmr_history_by_puuid",
        return_type=List[MMRHistoryPointV1],
        kwargs={"version": str, "region": str, "puuid": str},
    )
    MMR_HISTORY_BY_NAME = Endpoint(
        path="/valorant/{version}/mmr-history/{region}/{name}/{tag}",
        f_name="get_mmr_history_by_name",
        return_type=List[MMRHistoryPointV1],
        kwargs={"version": str, "region": str, "name": str, "tag": str},
    )
    MATCH_HISTORY_BY_PUUID = Endpoint(
        path="/valorant/{version}/by-puuid/matches/{region}/{puuid}",
        f_name="get_match_history_by_puuid",
        versions=["v3"],
        return_type=List[MatchHistoryPointV3],
        kwargs={
            "version": str,
            "region": str,
            "puuid": str,
            "size": Optional[int],
            "map": Optional[str],
            "game_mode": Optional[str],
        },
        query_args={
            "size": "{size}",
            "map": "{map}",
            "filter": "{game_mode}",
        },
    )
    MATCH_HISTORY_BY_NAME = Endpoint(
        path="/valorant/{version}/matches/{region}/{name}/{tag}",
        f_name="get_match_history_by_name",
        versions=["v3"],
        return_type=List[MatchHistoryPointV3],
        kwargs={
            "version": str,
            "region": str,
            "name": str,
            "tag": str,
            "size": Optional[int],
            "map": Optional[str],
            "game_mode": Optional[str],
        },
        query_args={
            "size": "{size}",
            "map": "{map}",
            "filter": "{game_mode}",
        },
    )
    LIFETIME_MATCHES_BY_PUUID = Endpoint(
        path="/valorant/{version}/by-puuid/lifetime/matches/{region}/{puuid}",
        f_name="get_lifetime_matches_by_puuid",
        return_type=List[LifetimeMatchV1],
        kwargs={
            "version": str,
            "region": str,
            "puuid": str,
            "mode": Optional[str],
            "map": Optional[str],
            "page": Optional[int],
            "size": Optional[int],
        },
        query_args={
            "mode": "{mode}",
            "map": "{map}",
            "page": "{page}",
            "size": "{size}",
        },
    )
    LIFETIME_MATCHES_BY_NAME = Endpoint(
        path="/valorant/{version}/lifetime/matches/{region}/{name}/{tag}",
        f_name="get_lifetime_matches_by_name",
        return_type=List[LifetimeMatchV1],
        kwargs={
            "version": str,
            "region": str,
            "name": str,
            "tag": str,
            "mode": Optional[str],
            "map": Optional[str],
            "page": Optional[int],
            "size": Optional[int],
        },
        query_args={
            "mode": "{mode}",
            "map": "{map}",
            "page": "{page}",
            "size": "{size}",
        },
    )
    CROSSHAIR = Endpoint(
        path="/valorant/{version}/crosshair/generate",
        f_name="get_crosshair",
        return_type=Image.Image,
        kwargs={
            "version": str,
            "crosshair_id": str,
        },
        query_args={
            "id": "{crosshair_id}",
        },
    )
