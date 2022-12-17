from typing import List

import msgspec.json

from valo_api.endpoints_config import EndpointsConfig
from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.error_response import ErrorResponse
from valo_api.responses.mmr_history import MMRHistoryPointV1
from valo_api.utils.fetch_endpoint import fetch_endpoint, response_type


def get_mmr_history_by_name_v1(
    region: str, name: str, tag: str, **kwargs
) -> List[MMRHistoryPointV1]:
    """Get MMR history by name for v1 of the endpoint.

    This is the same as :py:meth:`get_mmr_history_by_name(version="v1", region=region, name=name, tag=tag,
    **kwargs) <get_mmr_history_by_name>`

    Args:
        region: The region to get the MMR history from.
            One of the following:
            eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
        name: The name of the player to get the MMR history for.
        tag: The tag of the player to get the MMR history for.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        A list of :class:`.MMRHistoryPointV1` objects.
    """
    return get_mmr_history_by_name("v1", region, name, tag, **kwargs)


def get_mmr_history_by_puuid_v1(
    region: str, puuid: str, **kwargs
) -> List[MMRHistoryPointV1]:
    """Get MMR history by puuid for v1 of the endpoint.

    This is the same as :py:meth:`get_mmr_history_by_puuid(version="v1", region=region, puuid=puuid, **kwargs)
    <get_mmr_history_by_puuid>`

    Args:
        region: The region to get the MMR history from.
            One of the following:
            eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
        puuid: The puuid of the player to get the MMR history for.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        A list of :class:`.MMRHistoryPointV1` objects.
    """
    return get_mmr_history_by_puuid("v1", region, puuid, **kwargs)


def get_mmr_history_by_name(
    version: str, region: str, name: str, tag: str, **kwargs
) -> List[MMRHistoryPointV1]:
    """Get MMR history by name for a specific version of the endpoint.

    Args:
        version: The version of the endpoint to use.
            One of the following:
            v1 (Version 1), v2 (Version 2)
        region: The region to get the MMR history from.
            One of the following:
            eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
        name: The name of the player to get the MMR history for.
        tag: The tag of the player to get the MMR history for.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        A list of :class:`.MMRHistoryPointV1` objects.

    Raises:
        ValoAPIException: If the request failed.
    """
    response = fetch_endpoint(
        EndpointsConfig.MMR_HISTORY_BY_NAME,
        region=region,
        name=name,
        tag=tag,
        version=version,
        **kwargs,
    )

    if response.ok is False:
        error = msgspec.json.decode(response.content, type=ErrorResponse)
        error.headers = dict(response.headers)
        raise ValoAPIException(error)

    return msgspec.json.decode(
        response.content, type=response_type(List[MMRHistoryPointV1])
    ).data


def get_mmr_history_by_puuid(
    version: str, region: str, puuid: str, **kwargs
) -> List[MMRHistoryPointV1]:
    """Get MMR history by puuid for a specific version of the endpoint.

    Args:
        version: The version of the endpoint to use.
            One of the following:
            v1 (Version 1), v2 (Version 2)
        region: The region to get the MMR history from.
            One of the following:
            eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
        puuid: The puuid of the player to get the MMR history for.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        A list of :class:`.MMRHistoryPointV1` objects.

    Raises:
        ValoAPIException: If the request failed.
    """
    response = fetch_endpoint(
        EndpointsConfig.MMR_HISTORY_BY_PUUID,
        region=region,
        puuid=puuid,
        version=version,
        **kwargs,
    )

    if response.ok is False:
        error = msgspec.json.decode(response.content, type=ErrorResponse)
        error.headers = dict(response.headers)
        raise ValoAPIException(error)

    return msgspec.json.decode(
        response.content, type=response_type(List[MMRHistoryPointV1])
    ).data


try:

    from valo_api.utils.fetch_endpoint import fetch_endpoint_async

    async def get_mmr_history_by_name_v1_async(
        region: str, name: str, tag: str, **kwargs
    ) -> List[MMRHistoryPointV1]:
        """Get MMR history by name for v1 of the endpoint.

        This is the same as :py:meth:`get_mmr_history_by_name_async(version="v1", region=region, name=name, tag=tag,
        **kwargs) <get_mmr_history_by_name_async>`

        Args:
            region: The region to get the MMR history from.
                One of the following:
                eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
            name: The name of the player to get the MMR history for.
            tag: The tag of the player to get the MMR history for.
            **kwargs: Any additional arguments to pass to the endpoint.

        Returns:
            A list of :class:`.MMRHistoryPointV1` objects.
        """
        return await get_mmr_history_by_name_async("v1", region, name, tag, **kwargs)

    async def get_mmr_history_by_puuid_v1_async(
        region: str, puuid: str, **kwargs
    ) -> List[MMRHistoryPointV1]:
        """Get MMR history by puuid for v1 of the endpoint.

        This is the same as :py:meth:`get_mmr_history_by_puuid_async(version="v1", region=region, puuid=puuid, **kwargs)
        <get_mmr_history_by_puuid_async>`

        Args:
            region: The region to get the MMR history from.
                One of the following:
                eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
            puuid: The puuid of the player to get the MMR history for.
            **kwargs: Any additional arguments to pass to the endpoint.

        Returns:
            A list of :class:`.MMRHistoryPointV1` objects.
        """
        return await get_mmr_history_by_puuid_async("v1", region, puuid, **kwargs)

    async def get_mmr_history_by_name_async(
        version: str, region: str, name: str, tag: str, **kwargs
    ) -> List[MMRHistoryPointV1]:
        """Get MMR history by name for a specific version of the endpoint.

        Args:
            version: The version of the endpoint to use.
                One of the following:
                v1 (Version 1), v2 (Version 2)
            region: The region to get the MMR history from.
                One of the following:
                eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
            name: The name of the player to get the MMR history for.
            tag: The tag of the player to get the MMR history for.
            **kwargs: Any additional arguments to pass to the endpoint.

        Returns:
            A list of :class:`.MMRHistoryPointV1` objects.

        Raises:
            ValoAPIException: If the request failed.
        """
        response, content = await fetch_endpoint_async(
            EndpointsConfig.MMR_HISTORY_BY_NAME,
            region=region,
            name=name,
            tag=tag,
            version=version,
            **kwargs,
        )

        if response.ok is False:
            error = msgspec.json.decode(content, type=ErrorResponse)
            error.headers = dict(response.headers)
            raise ValoAPIException(error)

        return msgspec.json.decode(
            content, type=response_type(List[MMRHistoryPointV1])
        ).data

    async def get_mmr_history_by_puuid_async(
        version: str, region: str, puuid: str, **kwargs
    ) -> List[MMRHistoryPointV1]:
        """Get MMR history by puuid for a specific version of the endpoint.

        Args:
            version: The version of the endpoint to use.
                One of the following:
                v1 (Version 1), v2 (Version 2)
            region: The region to get the MMR history from.
                One of the following:
                eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
            puuid: The puuid of the player to get the MMR history for.
            **kwargs: Any additional arguments to pass to the endpoint.

        Returns:
            A list of :class:`.MMRHistoryPointV1` objects.

        Raises:
            ValoAPIException: If the request failed.
        """
        response, content = await fetch_endpoint_async(
            EndpointsConfig.MMR_HISTORY_BY_PUUID,
            region=region,
            puuid=puuid,
            version=version,
            **kwargs,
        )

        if response.ok is False:
            error = msgspec.json.decode(content, type=ErrorResponse)
            error.headers = dict(response.headers)
            raise ValoAPIException(error)

        return msgspec.json.decode(
            content, type=response_type(List[MMRHistoryPointV1])
        ).data

except ImportError:
    pass
