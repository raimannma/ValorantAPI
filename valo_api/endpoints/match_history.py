from typing import List, Union

from valo_api.endpoints_config import EndpointsConfig
from valo_api.responses.error_response import ErrorResponse
from valo_api.responses.match_history import MatchHistoryPointV3
from valo_api.utils.fetch_endpoint import fetch_endpoint


def get_match_history_by_name_v3(
    region: str, name: str, tag: str, **kwargs
) -> Union[List[MatchHistoryPointV3], ErrorResponse]:
    return get_match_history_by_name("v3", region, name, tag, **kwargs)


def get_match_history_by_puuid_v3(
    region: str, puuid: str, **kwargs
) -> Union[List[MatchHistoryPointV3], ErrorResponse]:
    return get_match_history_by_puuid("v3", region, puuid, **kwargs)


def get_match_history_by_name(
    version: str, region: str, name: str, tag: str, **kwargs
) -> Union[List[MatchHistoryPointV3], ErrorResponse]:
    response = fetch_endpoint(
        EndpointsConfig.MATCH_HISTORY_BY_NAME,
        version=version,
        region=region,
        name=name,
        tag=tag,
        **kwargs,
    )
    response_data = response.json()

    if response.ok is False:
        return ErrorResponse.from_dict(**response_data)

    return [MatchHistoryPointV3.from_dict(**match) for match in response_data["data"]]


def get_match_history_by_puuid(
    version: str, region: str, puuid: str, **kwargs
) -> Union[List[MatchHistoryPointV3], ErrorResponse]:
    response = fetch_endpoint(
        EndpointsConfig.MATCH_HISTORY_BY_PUUID,
        version=version,
        region=region,
        puuid=puuid,
        **kwargs,
    )
    response_data = response.json()

    if response.ok is False:
        return ErrorResponse.from_dict(**response_data)

    return [MatchHistoryPointV3.from_dict(**match) for match in response_data["data"]]
