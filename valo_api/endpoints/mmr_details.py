from typing import Optional, Union

from valo_api.endpoints_config import EndpointsConfig
from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.error_response import ErrorResponse
from valo_api.responses.mmr_details import MMRDetailsV1, MMRDetailsV2, SeasonDataV2
from valo_api.utils.fetch_endpoint import fetch_endpoint


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
    response_data = response.json()

    if response.ok is False:
        headers = dict(response.headers)
        raise ValoAPIException(
            ErrorResponse.from_dict(headers=headers, **response_data)
        )

    if version == "v1":
        return MMRDetailsV1.from_dict(**response_data["data"])
    elif version == "v2":
        try:
            if filter is None or filter == "":
                return MMRDetailsV2.from_dict(**response_data["data"])
            else:
                return SeasonDataV2.from_dict(**response_data["data"])
        except Exception:
            return MMRDetailsV2.from_dict(**response_data["data"])
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
    response_data = response.json()

    if response.ok is False:
        headers = dict(response.headers)
        raise ValoAPIException(
            ErrorResponse.from_dict(headers=headers, **response_data)
        )

    if version == "v1":
        cls = MMRDetailsV1
    elif version == "v2":
        try:
            if filter is None or filter == "":
                return MMRDetailsV2.from_dict(**response_data["data"])
            else:
                return SeasonDataV2.from_dict(**response_data["data"])
        except Exception:
            return MMRDetailsV2.from_dict(**response_data["data"])
    else:
        raise ValueError("Invalid version")

    return cls.from_dict(**response_data["data"])
