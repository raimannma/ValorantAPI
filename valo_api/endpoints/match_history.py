from typing import List, Optional

import warnings

import msgspec.json

from valo_api.endpoints_config import EndpointsConfig
from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.error_response import ErrorResponse
from valo_api.responses.match_history import MatchHistoryPointV3
from valo_api.utils.fetch_endpoint import fetch_endpoint, response_type


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
        size: The number of matches to return. Maximum is 10.
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
        size: The number of matches to return. Maximum is 10.
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
        size: The number of matches to return. Maximum is 10.
        game_mode: The game mode to filter by.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        A list of :class:`.MatchHistoryPointV3` objects.

    Raises:
        ValoAPIException: If the request failed.
    """
    query_args = dict()
    if size:
        if size > 10:
            warnings.warn(
                "You cannot fetch more then 10 matches with this endpoint. "
                "Size will be reduced to 10. "
                "See https://github.com/raimannma/ValorantAPI/issues/181 for a workaround."
            )
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

    if response.ok is False:
        error = msgspec.json.decode(response.content, type=ErrorResponse)
        error.headers = dict(response.headers)
        raise ValoAPIException(error)

    return msgspec.json.decode(
        response.content, type=response_type(List[MatchHistoryPointV3])
    ).data


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
        size: The number of matches to return. Maximum is 10.
        game_mode: The game mode to filter by.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        A list of :class:`.MatchHistoryPointV3` objects.

    Raises:
        ValoAPIException: If the request failed.
    """
    query_args = dict()
    if size:
        if size > 10:
            warnings.warn(
                "You cannot fetch more then 10 matches with this endpoint. "
                "Size will be reduced to 10. "
                "See https://github.com/raimannma/ValorantAPI/issues/181 for a workaround."
            )
            size = 10
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

    if response.ok is False:
        error = msgspec.json.decode(response.content, type=ErrorResponse)
        error.headers = dict(response.headers)
        raise ValoAPIException(error)

    return msgspec.json.decode(
        response.content, type=response_type(List[MatchHistoryPointV3])
    ).data


try:

    from valo_api.utils.fetch_endpoint import fetch_endpoint_async

    async def get_match_history_by_name_v3_async(
        region: str,
        name: str,
        tag: str,
        size: Optional[int] = None,
        game_mode: Optional[str] = None,
        **kwargs,
    ) -> List[MatchHistoryPointV3]:
        """Get the match history for a player by name and tag using version 3 of the endpoint.

        This is the same as :py:meth:`get_match_history_by_name_async(version="v3", region=region, name=name, tag=tag,
        size=size, game_mode=game_mode, **kwargs) <get_match_history_by_name_async>`

        Args:
            region: The region of the player.
                One of the following:
                eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
            name: The name of the player.
            tag: The tag of the player.
            size: The number of matches to return. Maximum is 10.
            game_mode: The game mode to filter by.
            **kwargs: Any additional arguments to pass to the endpoint.

        Returns:
            A list of :class:`.MatchHistoryPointV3` objects.
        """
        return await get_match_history_by_name_async(
            "v3", region, name, tag, size, game_mode, **kwargs
        )

    async def get_match_history_by_puuid_v3_async(
        region: str,
        puuid: str,
        size: Optional[int] = None,
        game_mode: Optional[str] = None,
        **kwargs,
    ) -> List[MatchHistoryPointV3]:
        """Get the match history for a player by puuid using version 3 of the endpoint.

        This is the same as :py:meth:`get_match_history_by_puuid_async(version="v3", region=region, puuid=puuid,
        size=size, game_mode=game_mode, **kwargs) <get_match_history_by_puuid_async>`

        Args:
            region: The region of the player.
                One of the following:
                eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
            puuid: The puuid of the player.
            size: The number of matches to return. Maximum is 10.
            game_mode: The game mode to filter by.
            **kwargs: Any additional arguments to pass to the endpoint.

        Returns:
            A list of :class:`.MatchHistoryPointV3` objects.
        """
        return await get_match_history_by_puuid_async(
            "v3", region, puuid, size, game_mode, **kwargs
        )

    async def get_match_history_by_name_async(
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
            size: The number of matches to return. Maximum is 10.
            game_mode: The game mode to filter by.
            **kwargs: Any additional arguments to pass to the endpoint.

        Returns:
            A list of :class:`.MatchHistoryPointV3` objects.

        Raises:
            ValoAPIException: If the request failed.
        """
        query_args = dict()
        if size:
            if size > 10:
                warnings.warn(
                    "You cannot fetch more then 10 matches with this endpoint. "
                    "Size will be reduced to 10. "
                    "See https://github.com/raimannma/ValorantAPI/issues/181 for a workaround."
                )
                size = 10
            query_args["size"] = str(size).lower()
        if game_mode:
            query_args["filter"] = game_mode.lower()
        response, content = await fetch_endpoint_async(
            EndpointsConfig.MATCH_HISTORY_BY_NAME,
            version=version,
            region=region,
            name=name,
            tag=tag,
            query_args=query_args,
            **kwargs,
        )

        if response.ok is False:
            error = msgspec.json.decode(content, type=ErrorResponse)
            error.headers = dict(response.headers)
            raise ValoAPIException(error)

        return msgspec.json.decode(
            content, type=response_type(List[MatchHistoryPointV3])
        ).data

    async def get_match_history_by_puuid_async(
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
            size: The number of matches to return. Maximum is 10.
            game_mode: The game mode to filter by.
            **kwargs: Any additional arguments to pass to the endpoint.

        Returns:
            A list of :class:`.MatchHistoryPointV3` objects.

        Raises:
            ValoAPIException: If the request failed.
        """
        query_args = dict()
        if size:
            if size > 10:
                warnings.warn(
                    "You cannot fetch more then 10 matches with this endpoint. "
                    "Size will be reduced to 10. "
                    "See https://github.com/raimannma/ValorantAPI/issues/181 for a workaround."
                )
                size = 10
            query_args["size"] = str(size).lower()
        if game_mode:
            query_args["filter"] = game_mode.lower()
        response, content = await fetch_endpoint_async(
            EndpointsConfig.MATCH_HISTORY_BY_PUUID,
            version=version,
            region=region,
            puuid=puuid,
            query_args=query_args,
            **kwargs,
        )

        if response.ok is False:
            error = msgspec.json.decode(content, type=ErrorResponse)
            error.headers = dict(response.headers)
            raise ValoAPIException(error)

        return msgspec.json.decode(
            content, type=response_type(List[MatchHistoryPointV3])
        ).data

except ImportError:
    pass
