from typing import List, Optional, Union

from valo_api.endpoints_config import EndpointsConfig
from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.error_response import ErrorResponse
from valo_api.responses.match_history import MatchHistoryPointV3
from valo_api.utils.fetch_endpoint import fetch_endpoint


def get_match_history_by_name_v3(
    region: str,
    name: str,
    tag: str,
    size: Optional[int] = None,
    game_mode: Optional[str] = None,
    **kwargs,
) -> Union[List[MatchHistoryPointV3], ErrorResponse]:
    return get_match_history_by_name("v3", region, name, tag, size, game_mode, **kwargs)


def get_match_history_by_puuid_v3(
    region: str,
    puuid: str,
    size: Optional[int] = None,
    game_mode: Optional[str] = None,
    **kwargs,
) -> Union[List[MatchHistoryPointV3], ErrorResponse]:
    return get_match_history_by_puuid("v3", region, puuid, size, game_mode, **kwargs)


def get_match_history_by_name(
    version: str,
    region: str,
    name: str,
    tag: str,
    size: Optional[int] = None,
    game_mode: Optional[str] = None,
    **kwargs,
) -> Union[List[MatchHistoryPointV3], ErrorResponse]:
    query_args = dict()
    if size:
        query_args["size"] = str(size).lower()
    if game_mode:
        query_args["filter"] = game_mode.lower()
    response = fetch_endpoint(
        EndpointsConfig.MATCH_HISTORY_BY_NAME,
        version=version,
        region=region,
        name=name,
        tag=tag,
        query_args=query_args,
        **kwargs,
    )
    response_data = response.json()

    if response.ok is False:
        raise ValoAPIException(ErrorResponse.from_dict(**response_data))

    return [MatchHistoryPointV3.from_dict(**match) for match in response_data["data"]]


def get_match_history_by_puuid(
    version: str,
    region: str,
    puuid: str,
    size: Optional[int] = None,
    game_mode: Optional[str] = None,
    **kwargs,
) -> Union[List[MatchHistoryPointV3], ErrorResponse]:
    query_args = dict()
    if size:
        query_args["size"] = str(size).lower()
    if game_mode:
        query_args["filter"] = game_mode.lower()
    response = fetch_endpoint(
        EndpointsConfig.MATCH_HISTORY_BY_PUUID,
        version=version,
        region=region,
        puuid=puuid,
        query_args=query_args,
        **kwargs,
    )
    response_data = response.json()

    if response.ok is False:
        raise ValoAPIException(ErrorResponse.from_dict(**response_data))

    return [MatchHistoryPointV3.from_dict(**match) for match in response_data["data"]]
