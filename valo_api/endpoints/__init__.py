from valo_api.endpoints.account_details import (
    get_account_details_by_name,
    get_account_details_by_name_v1,
    get_account_details_by_puuid,
    get_account_details_by_puuid_v1,
)
from valo_api.endpoints.content import get_content, get_content_v1
from valo_api.endpoints.crosshair import get_crosshair, get_crosshair_v1
from valo_api.endpoints.leaderboard import (
    get_leaderboard,
    get_leaderboard_v1,
    get_leaderboard_v2,
)
from valo_api.endpoints.match_details import get_match_details, get_match_details_v2
from valo_api.endpoints.match_history import (
    get_match_history_by_name,
    get_match_history_by_name_v3,
    get_match_history_by_puuid,
    get_match_history_by_puuid_v3,
)
from valo_api.endpoints.mmr_details import (
    get_mmr_details_by_name,
    get_mmr_details_by_name_v1,
    get_mmr_details_by_name_v2,
    get_mmr_details_by_puuid,
    get_mmr_details_by_puuid_v1,
    get_mmr_details_by_puuid_v2,
)
from valo_api.endpoints.mmr_history import (
    get_mmr_history_by_name,
    get_mmr_history_by_name_v1,
    get_mmr_history_by_puuid,
    get_mmr_history_by_puuid_v1,
)
from valo_api.endpoints.raw import get_raw_data, get_raw_data_v1
from valo_api.endpoints.status import get_status, get_status_v1
from valo_api.endpoints.store_featured import (
    get_store_featured,
    get_store_featured_v1,
    get_store_featured_v2,
)
from valo_api.endpoints.store_offers import get_store_offers, get_store_offers_v1
from valo_api.endpoints.version_info import get_version_info, get_version_info_v1
from valo_api.endpoints.website import get_website, get_website_v1

__all__ = [
    "get_account_details_by_name_v1",
    "get_account_details_by_name",
    "get_account_details_by_puuid_v1",
    "get_account_details_by_puuid",
    "get_content_v1",
    "get_content",
    "get_website_v1",
    "get_website",
    "get_version_info_v1",
    "get_version_info",
    "get_store_offers_v1",
    "get_store_offers",
    "get_store_featured_v1",
    "get_store_featured_v2",
    "get_store_featured",
    "get_status_v1",
    "get_status",
    "get_mmr_history_by_name_v1",
    "get_mmr_history_by_name",
    "get_mmr_history_by_puuid_v1",
    "get_mmr_history_by_puuid",
    "get_mmr_details_by_puuid_v1",
    "get_mmr_details_by_puuid_v2",
    "get_mmr_details_by_puuid",
    "get_mmr_details_by_name_v1",
    "get_mmr_details_by_name_v2",
    "get_mmr_details_by_name",
    "get_match_history_by_puuid_v3",
    "get_match_history_by_puuid",
    "get_match_history_by_name_v3",
    "get_match_history_by_name",
    "get_match_details_v2",
    "get_match_details",
    "get_leaderboard_v1",
    "get_leaderboard_v2",
    "get_leaderboard",
    "get_raw_data_v1",
    "get_raw_data",
    "get_crosshair_v1",
    "get_crosshair",
]

try:
    from valo_api.endpoints.account_details import (
        get_account_details_by_name_async,
        get_account_details_by_name_v1_async,
        get_account_details_by_puuid_async,
        get_account_details_by_puuid_v1_async,
    )
    from valo_api.endpoints.content import get_content_async, get_content_v1_async
    from valo_api.endpoints.crosshair import get_crosshair_async, get_crosshair_v1_async
    from valo_api.endpoints.leaderboard import (
        get_leaderboard_async,
        get_leaderboard_v1_async,
        get_leaderboard_v2_async,
    )
    from valo_api.endpoints.match_details import (
        get_match_details_async,
        get_match_details_v2_async,
    )
    from valo_api.endpoints.match_history import (
        get_match_history_by_name_async,
        get_match_history_by_name_v3_async,
        get_match_history_by_puuid_async,
        get_match_history_by_puuid_v3_async,
    )
    from valo_api.endpoints.mmr_details import (
        get_mmr_details_by_name_async,
        get_mmr_details_by_name_v1_async,
        get_mmr_details_by_name_v2_async,
        get_mmr_details_by_puuid_async,
        get_mmr_details_by_puuid_v1_async,
        get_mmr_details_by_puuid_v2_async,
    )
    from valo_api.endpoints.mmr_history import (
        get_mmr_history_by_name_async,
        get_mmr_history_by_name_v1_async,
        get_mmr_history_by_puuid_async,
        get_mmr_history_by_puuid_v1_async,
    )
    from valo_api.endpoints.raw import get_raw_data_async, get_raw_data_v1_async
    from valo_api.endpoints.status import get_status_async, get_status_v1_async
    from valo_api.endpoints.store_featured import (
        get_store_featured_async,
        get_store_featured_v1_async,
        get_store_featured_v2_async,
    )
    from valo_api.endpoints.store_offers import (
        get_store_offers_async,
        get_store_offers_v1_async,
    )
    from valo_api.endpoints.version_info import (
        get_version_info_async,
        get_version_info_v1_async,
    )
    from valo_api.endpoints.website import get_website_async, get_website_v1_async

    __all__.extend(
        [
            "get_account_details_by_name_v1_async",
            "get_account_details_by_puuid_v1_async",
            "get_account_details_by_name_async",
            "get_account_details_by_puuid_async",
            "get_content_v1_async",
            "get_content_async",
            "get_website_v1_async",
            "get_website_async",
            "get_version_info_v1_async",
            "get_version_info_async",
            "get_store_offers_v1_async",
            "get_store_offers_async",
            "get_store_featured_v1_async",
            "get_store_featured_v2_async",
            "get_store_featured_async",
            "get_status_v1_async",
            "get_status_async",
            "get_mmr_history_by_name_v1_async",
            "get_mmr_history_by_name_async",
            "get_mmr_history_by_puuid_v1_async",
            "get_mmr_history_by_puuid_async",
            "get_mmr_details_by_puuid_v1_async",
            "get_mmr_details_by_puuid_v2_async",
            "get_mmr_details_by_puuid_async",
            "get_mmr_details_by_name_v1_async",
            "get_mmr_details_by_name_v2_async",
            "get_mmr_details_by_name_async",
            "get_match_history_by_puuid_v3_async",
            "get_match_history_by_puuid_async",
            "get_match_history_by_name_v3_async",
            "get_match_history_by_name_async",
            "get_match_details_v2_async",
            "get_match_details_async",
            "get_leaderboard_v1_async",
            "get_leaderboard_v2_async",
            "get_leaderboard_async",
            "get_raw_data_v1_async",
            "get_raw_data_async",
            "get_crosshair_v1_async",
            "get_crosshair_async",
        ]
    )
except ImportError:
    pass
