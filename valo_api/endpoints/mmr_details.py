from typing import Optional, Union

import msgspec.json

from valo_api.endpoints_config import EndpointsConfig
from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.error_response import ErrorResponse
from valo_api.responses.mmr_details import MMRDetailsV1, MMRDetailsV2, SeasonDataV2
from valo_api.utils.fetch_endpoint import fetch_endpoint, response_type


def get_mmr_details_by_puuid_v1(region: str, puuid: str, **kwargs) -> MMRDetailsV1:
    """Get MMR details by puuid for v1 of the endpoint.

    This is the same as
    :py:meth:`get_mmr_details_by_puuid(version="v1", region=region, puuid=puuid, **kwargs) <get_mmr_details_by_puuid>`

    Args:
        region: The region to get the MMR details from.
            One of the following:
            eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
        puuid: The puuid to get the MMR details for.
        **kwargs: Any additional keyword arguments to pass to the endpoint.

    Returns:
        MMRDetailsV1: MMR Details fetched from the API.
    """
    return get_mmr_details_by_puuid("v1", region, puuid, **kwargs)


def get_mmr_details_by_puuid_v2(
    region: str, puuid: str, filter: Optional[str] = None, **kwargs
) -> Union[MMRDetailsV2, SeasonDataV2]:
    """Get MMR details by puuid for v2 of the endpoint.

    This is the same as
    :py:meth:`get_mmr_details_by_puuid(version="v2", region=region, puuid=puuid, **kwargs) <get_mmr_details_by_puuid>`

    Args:
        region: The region to get the MMR details from.
            One of the following:
            eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
        puuid: The puuid to get the MMR details for.
        filter: The filter to use for filtering data by season.
        **kwargs: Any additional keyword arguments to pass to the endpoint.

    Returns:
        - An :class:`.MMRDetailsV2` object.
        - An :class:`.SeasonDataV2` object.
    """
    return get_mmr_details_by_puuid("v2", region, puuid, filter, **kwargs)


def get_mmr_details_by_name_v1(
    region: str, name: str, tag: str, **kwargs
) -> MMRDetailsV1:
    """Get MMR details by name for v1 of the endpoint.

    This is the same as :py:meth:`get_mmr_details_by_name(version="v1", region=region, name=name, tag=tag,
    **kwargs) <get_mmr_details_by_name>`

    Args:
        region: The region to get the MMR details from.
            One of the following:
            eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
        name: The name to get the MMR details for.
        tag: The tag to get the MMR details for.
        **kwargs: Any additional keyword arguments to pass to the endpoint.

    Returns:
        MMRDetailsV1: MMR Details fetched from the API.
    """
    return get_mmr_details_by_name("v1", region, name, tag, **kwargs)


def get_mmr_details_by_name_v2(
    region: str, name: str, tag: str, filter: Optional[str] = None, **kwargs
) -> Union[MMRDetailsV2, SeasonDataV2]:
    """Get MMR details by name for v2 of the endpoint.

    This is the same as :py:meth:`get_mmr_details_by_name(version="v2", region=region, name=name, tag=tag,
    **kwargs) <get_mmr_details_by_name>`

    Args:
        region: The region to get the MMR details from.
            One of the following:
            eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
        name: The name to get the MMR details for.
        tag: The tag to get the MMR details for.
        filter: The filter to use for filtering data by season.
        **kwargs: Any additional keyword arguments to pass to the endpoint.

    Returns:
        - An :class:`.MMRDetailsV2` object.
        - An :class:`.SeasonDataV2` object.
    """
    return get_mmr_details_by_name("v2", region, name, tag, filter, **kwargs)


def get_mmr_details_by_name(
    version: str,
    region: str,
    name: str,
    tag: str,
    filter: Optional[str] = None,
    **kwargs,
) -> Union[MMRDetailsV1, MMRDetailsV2, SeasonDataV2]:
    """Get MMR details by name for a specific endpoint version.

    Args:
        version: The version of the endpoint to use.
        region: The region to get the MMR details from.
            One of the following:
            eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
        name: The name to get the MMR details for.
        tag: The tag to get the MMR details for.
        filter: The filter to use for filtering data by season.
        **kwargs: Any additional keyword arguments to pass to the endpoint.

    Returns:
        - An :class:`.MMRDetailsV1` object.
        - An :class:`.MMRDetailsV2` object.
        - An :class:`.SeasonDataV2` object.

    Raises:
        ValoAPIException: If the request failed.
        ValueError: If the version is not one of the supported versions.
    """
    response = fetch_endpoint(
        EndpointsConfig.MMR_DETAILS_BY_NAME,
        region=region,
        name=name,
        tag=tag,
        version=version,
        query_args={"filter": str(filter).lower()} if filter is not None else None,
        **kwargs,
    )

    if response.ok is False:
        error = msgspec.json.decode(response.content, type=ErrorResponse)
        error.headers = dict(response.headers)
        raise ValoAPIException(error)

    if version == "v1":
        return msgspec.json.decode(
            response.content, type=response_type(MMRDetailsV1)
        ).data
    elif version == "v2":
        try:
            if filter is None or filter == "":
                return msgspec.json.decode(
                    response.content, type=response_type(MMRDetailsV2)
                ).data
            else:
                return msgspec.json.decode(
                    response.content, type=response_type(SeasonDataV2)
                ).data
        except Exception:
            return msgspec.json.decode(
                response.content, type=response_type(MMRDetailsV2)
            ).data
    else:
        raise ValueError("Invalid version")


def get_mmr_details_by_puuid(
    version: str, region: str, puuid: str, filter: Optional[str] = None, **kwargs
) -> Union[MMRDetailsV1, MMRDetailsV2, SeasonDataV2]:
    """Get MMR details by puuid for a specific endpoint version.

    Args:
        version: The version of the endpoint to use.
        region: The region to get the MMR details from.
            One of the following:
            eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
        puuid: The puuid to get the MMR details for.
        filter: The filter to use for filtering data by season.
        **kwargs: Any additional keyword arguments to pass to the endpoint.

    Returns:
        - An :class:`.MMRDetailsV1` object.
        - An :class:`.MMRDetailsV2` object.
        - An :class:`.SeasonDataV2` object.

    Raises:
        ValoAPIException: If the request failed.
        ValueError: If the version is not one of the supported versions.
    """
    response = fetch_endpoint(
        EndpointsConfig.MMR_DETAILS_BY_PUUID,
        region=region,
        puuid=puuid,
        version=version,
        query_args={"filter": str(filter).lower()} if filter is not None else None,
        **kwargs,
    )

    if response.ok is False:
        error = msgspec.json.decode(response.content, type=ErrorResponse)
        error.headers = dict(response.headers)
        raise ValoAPIException(error)

    if version == "v1":
        return msgspec.json.decode(
            response.content, type=response_type(MMRDetailsV1)
        ).data
    elif version == "v2":
        try:
            if filter is None or filter == "":
                return msgspec.json.decode(
                    response.content, type=response_type(MMRDetailsV2)
                ).data
            else:
                return msgspec.json.decode(
                    response.content, type=response_type(SeasonDataV2)
                ).data
        except Exception:
            return msgspec.json.decode(
                response.content, type=response_type(MMRDetailsV2)
            ).data
    else:
        raise ValueError("Invalid version")


try:

    from valo_api.utils.fetch_endpoint import fetch_endpoint_async

    async def get_mmr_details_by_name_v1_async(
        region: str,
        name: str,
        tag: str,
        filter: Optional[str] = None,
        **kwargs,
    ) -> MMRDetailsV1:
        """Get MMR details by name for v1 of the endpoint.

        This is the same as :py:meth:`get_mmr_details_by_name_async(version="v1", region=region, name=name, tag=tag,
        filter=filter, **kwargs) <get_mmr_details_by_name_async>`

        Args:
            region: The region to get the MMR details from.
                One of the following:
                eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
            name: The name to get the MMR details for.
            tag: The tag to get the MMR details for.
            filter: The filter to use for filtering data by season.
            **kwargs: Any additional keyword arguments to pass to the endpoint.

        Returns:
            MMRDetailsV1: An :class:`.MMRDetailsV1` object.
        """
        return await get_mmr_details_by_name_async(
            "v1", region, name, tag, filter, **kwargs
        )

    async def get_mmr_details_by_name_v2_async(
        region: str,
        name: str,
        tag: str,
        filter: Optional[str] = None,
        **kwargs,
    ) -> Union[MMRDetailsV2, SeasonDataV2]:
        """Get MMR details by name for v2 of the endpoint.

        This is the same as :py:meth:`get_mmr_details_by_name_async(version="v2", region=region, name=name, tag=tag,
        filter=filter, **kwargs) <get_mmr_details_by_name_async>`

        Args:
            region: The region to get the MMR details from.
                One of the following:
                eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
            name: The name to get the MMR details for.
            tag: The tag to get the MMR details for.
            filter: The filter to use for filtering data by season.
            **kwargs: Any additional keyword arguments to pass to the endpoint.

        Returns:
            - An :class:`.MMRDetailsV2` object.
            - An :class:`.SeasonDataV2` object.
        """
        return await get_mmr_details_by_name_async(
            "v2", region, name, tag, filter, **kwargs
        )

    async def get_mmr_details_by_name_async(
        version: str,
        region: str,
        name: str,
        tag: str,
        filter: Optional[str] = None,
        **kwargs,
    ) -> Union[MMRDetailsV1, MMRDetailsV2, SeasonDataV2]:
        """Get MMR details by name for a specific endpoint version.

        Args:
            version: The version of the endpoint to use.
            region: The region to get the MMR details from.
                One of the following:
                eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
            name: The name to get the MMR details for.
            tag: The tag to get the MMR details for.
            filter: The filter to use for filtering data by season.
            **kwargs: Any additional keyword arguments to pass to the endpoint.

        Returns:
            - An :class:`.MMRDetailsV1` object.
            - An :class:`.MMRDetailsV2` object.
            - An :class:`.SeasonDataV2` object.

        Raises:
            ValoAPIException: If the request failed.
            ValueError: If the version is not one of the supported versions.
        """
        response, content = await fetch_endpoint_async(
            EndpointsConfig.MMR_DETAILS_BY_NAME,
            region=region,
            name=name,
            tag=tag,
            version=version,
            query_args={"filter": str(filter).lower()} if filter is not None else None,
            **kwargs,
        )

        if response.ok is False:
            error = msgspec.json.decode(content, type=ErrorResponse)
            error.headers = dict(response.headers)
            raise ValoAPIException(error)

        if version == "v1":
            return msgspec.json.decode(content, type=response_type(MMRDetailsV1)).data
        elif version == "v2":
            try:
                if filter is None or filter == "":
                    return msgspec.json.decode(
                        content, type=response_type(MMRDetailsV2)
                    ).data
                else:
                    return msgspec.json.decode(
                        content, type=response_type(SeasonDataV2)
                    ).data
            except Exception:
                return msgspec.json.decode(
                    content, type=response_type(MMRDetailsV2)
                ).data
        else:
            raise ValueError("Invalid version")

    async def get_mmr_details_by_puuid_v1_async(
        region: str,
        puuid: str,
        filter: Optional[str] = None,
        **kwargs,
    ) -> MMRDetailsV1:
        """Get MMR details by puuid for v1 of the endpoint.

        This is the same as :py:meth:`get_mmr_details_by_puuid_async(version="v1", region=region, puuid=puuid, filter=filter,
        **kwargs) <get_mmr_details_by_puuid_async>`

        Args:
            region: The region to get the MMR details from.
                One of the following:
                eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
            puuid: The puuid to get the MMR details for.
            filter: The filter to use for filtering data by season.
            **kwargs: Any additional keyword arguments to pass to the endpoint.

        Returns:
            MMRDetailsV1: An :class:`.MMRDetailsV1` object.
        """
        return await get_mmr_details_by_puuid_async(
            "v1", region, puuid, filter, **kwargs
        )

    async def get_mmr_details_by_puuid_v2_async(
        region: str,
        puuid: str,
        filter: Optional[str] = None,
        **kwargs,
    ) -> Union[MMRDetailsV2, SeasonDataV2]:
        """Get MMR details by puuid for v2 of the endpoint.

        This is the same as :py:meth:`get_mmr_details_by_puuid_async(version="v2", region=region, puuid=puuid, filter=filter,
        **kwargs) <get_mmr_details_by_puuid_async>`

        Args:
            region: The region to get the MMR details from.
                One of the following:
                eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
            puuid: The puuid to get the MMR details for.
            filter: The filter to use for filtering data by season.
            **kwargs: Any additional keyword arguments to pass to the endpoint.

        Returns:
            - An :class:`.MMRDetailsV2` object.
            - An :class:`.SeasonDataV2` object.
        """
        return await get_mmr_details_by_puuid_async(
            "v2", region, puuid, filter, **kwargs
        )

    async def get_mmr_details_by_puuid_async(
        version: str, region: str, puuid: str, filter: Optional[str] = None, **kwargs
    ) -> Union[MMRDetailsV1, MMRDetailsV2, SeasonDataV2]:
        """Get MMR details by puuid for a specific endpoint version.

        Args:
            version: The version of the endpoint to use.
            region: The region to get the MMR details from.
                One of the following:
                eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
            puuid: The puuid to get the MMR details for.
            filter: The filter to use for filtering data by season.
            **kwargs: Any additional keyword arguments to pass to the endpoint.

        Returns:
            - An :class:`.MMRDetailsV1` object.
            - An :class:`.MMRDetailsV2` object.
            - An :class:`.SeasonDataV2` object.

        Raises:
            ValoAPIException: If the request failed.
            ValueError: If the version is not one of the supported versions.
        """
        response, content = await fetch_endpoint_async(
            EndpointsConfig.MMR_DETAILS_BY_PUUID,
            region=region,
            puuid=puuid,
            version=version,
            query_args={"filter": str(filter).lower()} if filter is not None else None,
            **kwargs,
        )

        if response.ok is False:
            error = msgspec.json.decode(content, type=ErrorResponse)
            error.headers = dict(response.headers)
            raise ValoAPIException(error)

        if version == "v1":
            return msgspec.json.decode(content, type=response_type(MMRDetailsV1)).data
        elif version == "v2":
            try:
                if filter is None or filter == "":
                    return msgspec.json.decode(
                        content, type=response_type(MMRDetailsV2)
                    ).data
                else:
                    return msgspec.json.decode(
                        content, type=response_type(SeasonDataV2)
                    ).data
            except Exception:
                return msgspec.json.decode(
                    content, type=response_type(MMRDetailsV2)
                ).data
        else:
            raise ValueError("Invalid version")

except ImportError:
    pass
