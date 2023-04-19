from typing import List, Optional

import msgspec.json

from valo_api.endpoints_config import EndpointsConfig
from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.error_response import ErrorResponse
from valo_api.responses.lifetime_match import LifetimeMatchV1
from valo_api.utils.fetch_endpoint import fetch_endpoint, response_type


def get_lifetime_matches_by_name_v1(
    region: str,
    name: str,
    tag: str,
    mode: Optional[str] = None,
    map: Optional[str] = None,
    page: Optional[int] = None,
    size: Optional[int] = None,
    **kwargs,
) -> LifetimeMatchV1:
    """Get the lifetime matches for a player by name using version 1 of the endpoint.

    This is the same as
    :py:meth:`get_lifetime_matches_by_name(version="v1", region=region, name=name, tag=tag, mode=mode, map=map, page=page, size=size, **kwargs) <get_lifetime_matches_by_name>`

    Args:
        region: The region to get the match history for.
        name: The player's name to get the match history for.
        tag: The player's tag to get the match history for.
        mode: The game mode to get the match history for.
        map: The map to get the match history for.
        page: The page of the match history to get.
        size: The number of matches to get per page.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        LifetimeMatchV1: Match history fetched from the API.

    Raises:
        ValoAPIException: If the request failed.
    """
    return get_lifetime_matches_by_name(
        version="v1",
        region=region,
        name=name,
        tag=tag,
        mode=mode,
        map=map,
        page=page,
        size=size,
        **kwargs,
    )


def get_lifetime_matches_by_name(
    version: str,
    region: str,
    name: str,
    tag: str,
    mode: Optional[str] = None,
    map: Optional[str] = None,
    page: Optional[int] = None,
    size: Optional[int] = None,
    **kwargs,
) -> LifetimeMatchV1:
    """Get the lifetime matches for a player by name.

    Args:
        version: The version of the endpoint to use.
        region: The region to get the match history for.
        name: The player's name to get the match history for.
        tag: The player's tag to get the match history for.
        mode: The game mode to get the match history for.
        map: The map to get the match history for.
        page: The page of the match history to get.
        size: The number of matches to get per page.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        LifetimeMatchV1: Match history fetched from the API.

    Raises:
        ValoAPIException: If the request failed.
    """
    assert (size is None) is (page is None), "Page and size must be used together."
    assert page is None or page > 0, f"Page must be greater than 0, got {page}."

    query_args = {}
    if mode is not None:
        query_args["mode"] = mode
    if map is not None:
        query_args["map"] = map
    if page is not None:
        query_args["page"] = page
    if size is not None:
        query_args["size"] = size

    response = fetch_endpoint(
        EndpointsConfig.LIFETIME_MATCHES_BY_NAME,
        version=version,
        query_args=query_args,
        region=region,
        name=name,
        tag=tag,
        **kwargs,
    )

    if response.ok is False:
        print(response.content)
        error = msgspec.json.decode(response.content, type=ErrorResponse)
        error.headers = dict(response.headers)
        raise ValoAPIException(error)

    return msgspec.json.decode(
        response.content, type=response_type(List[LifetimeMatchV1])
    ).data


def get_lifetime_matches_by_puuid_v1(
    region: str,
    puuid: str,
    mode: Optional[str] = None,
    map: Optional[str] = None,
    page: Optional[int] = None,
    size: Optional[int] = None,
    **kwargs,
) -> LifetimeMatchV1:
    """Get the lifetime matches for a player by puuid using version 1 of the endpoint.

    This is the same as
    :py:meth:`get_lifetime_matches_by_puuid(version="v1", region=region, puuid=puuid, mode=mode, map=map, page=page, size=size, **kwargs) <get_lifetime_matches_by_puuid>`

    Args:
        region: The region to get the match history for.
        puuid: The player's PUUID to get the match history for.
        mode: The game mode to get the match history for.
        map: The map to get the match history for.
        page: The page of the match history to get.
        size: The number of matches to get per page.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        LifetimeMatchV1: Match history fetched from the API.

    Raises:
        ValoAPIException: If the request failed.
    """
    return get_lifetime_matches_by_puuid(
        version="v1",
        region=region,
        puuid=puuid,
        mode=mode,
        map=map,
        page=page,
        size=size,
        **kwargs,
    )


def get_lifetime_matches_by_puuid(
    version: str,
    region: str,
    puuid: str,
    mode: Optional[str] = None,
    map: Optional[str] = None,
    page: Optional[int] = None,
    size: Optional[int] = None,
    **kwargs,
) -> LifetimeMatchV1:
    """Get the lifetime matches for a player by puuid.

    Args:
        version: The version of the endpoint to use.
        region: The region to get the match history for.
        puuid: The player's PUUID to get the match history for.
        mode: The game mode to get the match history for.
        map: The map to get the match history for.
        page: The page of the match history to get.
        size: The number of matches to get per page.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        LifetimeMatchV1: Match history fetched from the API.

    Raises:
        ValoAPIException: If the request failed.
    """
    assert (size is None) is (page is None), "Page and size must be used together."
    assert page is None or page > 0, f"Page must be greater than 0, got {page}."

    query_args = {}
    if mode is not None:
        query_args["mode"] = mode
    if map is not None:
        query_args["map"] = map
    if page is not None:
        query_args["page"] = page
    if size is not None:
        query_args["size"] = size

    response = fetch_endpoint(
        EndpointsConfig.LIFETIME_MATCHES_BY_PUUID,
        version=version,
        query_args=query_args,
        region=region,
        puuid=puuid,
        **kwargs,
    )

    if response.ok is False:
        print(response.content)
        error = msgspec.json.decode(response.content, type=ErrorResponse)
        error.headers = dict(response.headers)
        raise ValoAPIException(error)

    return msgspec.json.decode(
        response.content, type=response_type(List[LifetimeMatchV1])
    ).data


try:
    from valo_api.utils.fetch_endpoint import fetch_endpoint_async

    async def get_lifetime_matches_by_name_v1_async(
        region: str,
        name: str,
        tag: str,
        mode: Optional[str] = None,
        map: Optional[str] = None,
        page: Optional[int] = None,
        size: Optional[int] = None,
        **kwargs,
    ) -> LifetimeMatchV1:
        """Get the lifetime matches for a player by name using version 1 of the endpoint.

        This is the same as
        :py:meth:`get_lifetime_matches_by_name(version="v1", region=region, name=name, tag=tag, mode=mode, map=map, page=page, size=size, **kwargs) <get_lifetime_matches_by_name>`

        Args:
            region: The region to get the match history for.
            name: The player's name to get the match history for.
            tag: The player's tag to get the match history for.
            mode: The game mode to get the match history for.
            map: The map to get the match history for.
            page: The page of the match history to get.
            size: The number of matches to get per page.
            **kwargs: Any additional arguments to pass to the endpoint.

        Returns:
            LifetimeMatchV1: Match history fetched from the API.

        Raises:
            ValoAPIException: If the request failed.
        """
        return await get_lifetime_matches_by_name_async(
            version="v1",
            region=region,
            name=name,
            tag=tag,
            mode=mode,
            map=map,
            page=page,
            size=size,
            **kwargs,
        )

    async def get_lifetime_matches_by_name_async(
        version: str,
        region: str,
        name: str,
        tag: str,
        mode: Optional[str] = None,
        map: Optional[str] = None,
        page: Optional[int] = None,
        size: Optional[int] = None,
        **kwargs,
    ) -> LifetimeMatchV1:
        """Get the lifetime matches for a player by name.

        Args:
            version: The version of the endpoint to use.
            region: The region to get the match history for.
            name: The player's name to get the match history for.
            tag: The player's tag to get the match history for.
            mode: The game mode to get the match history for.
            map: The map to get the match history for.
            page: The page of the match history to get.
            size: The number of matches to get per page.
            **kwargs: Any additional arguments to pass to the endpoint.

        Returns:
            LifetimeMatchV1: Match history fetched from the API.

        Raises:
            ValoAPIException: If the request failed.
        """
        assert (size is None) is (page is None), "Page and size must be used together."
        assert page is None or page > 0, f"Page must be greater than 0, got {page}."

        query_args = {}
        if mode is not None:
            query_args["mode"] = mode
        if map is not None:
            query_args["map"] = map
        if page is not None:
            query_args["page"] = page
        if size is not None:
            query_args["size"] = size

        response, content = await fetch_endpoint_async(
            EndpointsConfig.LIFETIME_MATCHES_BY_NAME,
            version=version,
            query_args=query_args,
            region=region,
            name=name,
            tag=tag,
            **kwargs,
        )

        if response.ok is False:
            error = msgspec.json.decode(content, type=ErrorResponse)
            error.headers = dict(response.headers)
            raise ValoAPIException(error)

        return msgspec.json.decode(
            content, type=response_type(List[LifetimeMatchV1])
        ).data

    async def get_lifetime_matches_by_puuid_v1_async(
        region: str,
        puuid: str,
        mode: Optional[str] = None,
        map: Optional[str] = None,
        page: Optional[int] = None,
        size: Optional[int] = None,
        **kwargs,
    ) -> LifetimeMatchV1:
        """Get the lifetime matches for a player by puuid using version 1 of the endpoint.

        This is the same as
        :py:meth:`get_lifetime_matches_by_puuid(version="v1", region=region, puuid=puuid, mode=mode, map=map, page=page, size=size, **kwargs) <get_lifetime_matches_by_puuid>`

        Args:
            region: The region to get the match history for.
            puuid: The player's PUUID to get the match history for.
            mode: The game mode to get the match history for.
            map: The map to get the match history for.
            page: The page of the match history to get.
            size: The number of matches to get per page.
            **kwargs: Any additional arguments to pass to the endpoint.

        Returns:
            LifetimeMatchV1: Match history fetched from the API.

        Raises:
            ValoAPIException: If the request failed.
        """
        return await get_lifetime_matches_by_puuid(
            version="v1",
            region=region,
            puuid=puuid,
            mode=mode,
            map=map,
            page=page,
            size=size,
            **kwargs,
        )

    async def get_lifetime_matches_by_puuid_async(
        version: str,
        region: str,
        puuid: str,
        mode: Optional[str] = None,
        map: Optional[str] = None,
        page: Optional[int] = None,
        size: Optional[int] = None,
        **kwargs,
    ) -> LifetimeMatchV1:
        """Get the lifetime matches for a player by puuid.

        Args:
            version: The version of the endpoint to use.
            region: The region to get the match history for.
            puuid: The player's PUUID to get the match history for.
            mode: The game mode to get the match history for.
            map: The map to get the match history for.
            page: The page of the match history to get.
            size: The number of matches to get per page.
            **kwargs: Any additional arguments to pass to the endpoint.

        Returns:
            LifetimeMatchV1: Match history fetched from the API.

        Raises:
            ValoAPIException: If the request failed.
        """
        assert (size is None) is (page is None), "Page and size must be used together."
        assert page is None or page > 0, f"Page must be greater than 0, got {page}."

        query_args = {}
        if mode is not None:
            query_args["mode"] = mode
        if map is not None:
            query_args["map"] = map
        if page is not None:
            query_args["page"] = page
        if size is not None:
            query_args["size"] = size

        response, content = await fetch_endpoint_async(
            EndpointsConfig.LIFETIME_MATCHES_BY_PUUID,
            version=version,
            query_args=query_args,
            region=region,
            puuid=puuid,
            **kwargs,
        )

        if response.ok is False:
            error = msgspec.json.decode(content, type=ErrorResponse)
            error.headers = dict(response.headers)
            raise ValoAPIException(error)

        return msgspec.json.decode(
            content, type=response_type(List[LifetimeMatchV1])
        ).data

except ImportError:
    pass
