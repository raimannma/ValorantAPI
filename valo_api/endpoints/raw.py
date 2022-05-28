from typing import Optional, Union

import urllib
from enum import Enum

from valo_api.endpoints_config import EndpointsConfig
from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.competitive_updates_raw import CompetitiveUpdatesRawV1
from valo_api.responses.error_response import ErrorResponse
from valo_api.responses.match_details_raw import MatchDetailsRawV1
from valo_api.responses.match_history_raw import MatchHistoryRawV1
from valo_api.responses.mmr_raw import MMRRawV1
from valo_api.utils.fetch_endpoint import fetch_endpoint


class EndpointType(Enum):
    COMPETITIVE_UPDATES = "competitiveupdates"
    MMR = "mmr"
    MATCH_DETAILS = "matchdetails"
    MATCH_HISTORY = "matchhistory"


def get_raw_data_v1(
    type: EndpointType,
    value: Optional[str] = None,
    region: Optional[str] = None,
    queries: Optional[dict] = None,
    **kwargs,
) -> Union[MMRRawV1, MatchHistoryRawV1, CompetitiveUpdatesRawV1, MatchDetailsRawV1]:
    return get_raw_data("v1", type, value, region, queries, **kwargs)


def get_raw_data(
    version: str,
    type: EndpointType,
    value: Optional[str] = None,
    region: Optional[str] = None,
    queries: Optional[dict] = None,
    **kwargs,
) -> Union[MMRRawV1, MatchHistoryRawV1, CompetitiveUpdatesRawV1, MatchDetailsRawV1]:
    query_args = {
        "type": type.value,
    }
    if value is not None:
        query_args["value"] = value
    if region is not None:
        query_args["region"] = region
    if queries is not None and len(queries) > 0:
        query_args["queries"] = f"?{urllib.parse.urlencode(queries)}"

    response = fetch_endpoint(
        EndpointsConfig.RAW,
        version=version,
        method="POST",
        query_args=query_args,
        **kwargs,
    )
    response_data = response.json()

    if response.ok is False:
        raise ValoAPIException(ErrorResponse.from_dict(**response_data))

    if type == EndpointType.MATCH_DETAILS:
        return MatchDetailsRawV1.from_dict(**response_data)
    elif type == EndpointType.COMPETITIVE_UPDATES:
        return CompetitiveUpdatesRawV1.from_dict(**response_data)
    elif type == EndpointType.MMR:
        return MMRRawV1.from_dict(**response_data)
    elif type == EndpointType.MATCH_HISTORY:
        return MatchHistoryRawV1.from_dict(**response_data)

    raise ValueError(f"Unknown endpoint type: {type}")
