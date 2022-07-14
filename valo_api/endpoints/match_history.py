from typing import List, Optional

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
) -> List[MatchHistoryPointV3]:
    """Get the match history for a player by name and tag using version 3 of the endpoint.

    This is the same as :py:meth:`get_match_history_by_name(version="v3", region=region, name=name, tag=tag,
    size=size, game_mode=game_mode, **kwargs) <get_match_history_by_name>`

    Args:
        region: The region of the player.
            One of the following:
            eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
        name: The name of the player.
        tag: The tag of the player.
        size: The number of matches to return.
        game_mode: The game mode to filter by.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        A list of :class:`.MatchHistoryPointV3` objects.
    """
    return get_match_history_by_name("v3", region, name, tag, size, game_mode, **kwargs)


def get_match_history_by_puuid_v3(
    region: str,
    puuid: str,
    size: Optional[int] = None,
    game_mode: Optional[str] = None,
    **kwargs,
) -> List[MatchHistoryPointV3]:
    """Get the match history for a player by puuid using version 3 of the endpoint.

    This is the same as :py:meth:`get_match_history_by_puuid(version="v3", region=region, puuid=puuid, size=size,
    game_mode=game_mode, **kwargs) <get_match_history_by_puuid>`

    Args:
        region: The region of the player.
            One of the following:
            eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
        puuid: The puuid of the player.
        size: The number of matches to return.
        game_mode: The game mode to filter by.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        A list of :class:`.MatchHistoryPointV3` objects.
    """
    return get_match_history_by_puuid("v3", region, puuid, size, game_mode, **kwargs)


def get_match_history_by_name(
    version: str,
    region: str,
    name: str,
    tag: str,
    size: Optional[int] = None,
    game_mode: Optional[str] = None,
    **kwargs,
) -> List[MatchHistoryPointV3]:
    """Get the match history for a player by name and tag using a specific version of the endpoint.

    Args:
        version: The version of the endpoint to use.
            One of the following:
            v3 (Version 3)
        region: The region of the player.
            One of the following:
            eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
        name: The name of the player.
        tag: The tag of the player.
        size: The number of matches to return.
        game_mode: The game mode to filter by.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        A list of :class:`.MatchHistoryPointV3` objects.

    Raises:
        ValoAPIException: If the request failed.
    """
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
        headers = dict(response.headers)
        raise ValoAPIException(
            ErrorResponse.from_dict(headers=headers, **response_data)
        )

    return [MatchHistoryPointV3.from_dict(**match) for match in response_data["data"]]


def get_match_history_by_puuid(
    version: str,
    region: str,
    puuid: str,
    size: Optional[int] = None,
    game_mode: Optional[str] = None,
    **kwargs,
) -> List[MatchHistoryPointV3]:
    """Get the match history for a player by puuid using a specific version of the endpoint.

    Args:
        version: The version of the endpoint to use.
            One of the following:
            v3 (Version 3)
        region: The region of the player.
            One of the following:
            eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
        puuid: The puuid of the player.
        size: The number of matches to return.
        game_mode: The game mode to filter by.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        A list of :class:`.MatchHistoryPointV3` objects.

    Raises:
        ValoAPIException: If the request failed.
    """
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
        headers = dict(response.headers)
        raise ValoAPIException(
            ErrorResponse.from_dict(headers=headers, **response_data)
        )

    return [MatchHistoryPointV3.from_dict(**match) for match in response_data["data"]]
