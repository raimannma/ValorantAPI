from typing import Union

from valo_api.endpoints_config import EndpointsConfig
from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.error_response import ErrorResponse
from valo_api.responses.match_history import MatchHistoryPointV3
from valo_api.utils.fetch_endpoint import fetch_endpoint


def get_match_details_v2(
    matchId: str, **kwargs
) -> Union[MatchHistoryPointV3, ErrorResponse]:
    return get_match_details("v2", matchId, **kwargs)


def get_match_details(
    version: str, matchId: str, **kwargs
) -> Union[MatchHistoryPointV3, ErrorResponse]:
    response = fetch_endpoint(
        EndpointsConfig.MATCH_DETAILS,
        version=version,
        matchId=matchId,
        **kwargs,
    )
    response_data = response.json()

    if response.ok is False:
        raise ValoAPIException(ErrorResponse.from_dict(**response_data))

    return MatchHistoryPointV3.from_dict(**response_data["data"])
