from typing import List, Optional, Union

from valo_api.endpoints_config import EndpointsConfig
from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.error_response import ErrorResponse
from valo_api.responses.store_featured import BundleV2, StoreFeaturedV1
from valo_api.utils.fetch_endpoint import fetch_endpoint


def get_store_featured_v1(**kwargs) -> StoreFeaturedV1:
    """Get the store featured using version 1 of the endpoint.

    This is the same as
    :py:meth:`get_store_featured(version="v1", **kwargs) <get_store_featured>`

    Args:
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        StoreFeaturedV1: Store featured fetched from the API.
    """
    return get_store_featured("v1", **kwargs)


def get_store_featured_v2(**kwargs) -> List[BundleV2]:
    """Get the store featured using version 2 of the endpoint.

    This is the same as
    :py:meth:`get_store_featured(version="v2", **kwargs) <get_store_featured>`

    Args:
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        List[BundleV2]: Bundles featured fetched from the API.
    """
    return get_store_featured("v2", **kwargs)


def get_store_featured(
    version: str, **kwargs
) -> Union[StoreFeaturedV1, List[BundleV2]]:
    """Get the store featured using a specific version of the endpoint.

    Args:
        version: The version of the endpoint to use.
            One of the following:
            v1 (Version 1)
            v2 (Version 2)
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        StoreFeaturedV1: Store featured fetched from the API.
        List[BundleV2]: Bundles featured fetched from the API.

    Raises:
        ValoAPIException: If the request failed.
    """
    response = fetch_endpoint(
        EndpointsConfig.STORE_FEATURED,
        version=version,
        **kwargs,
    )
    response_data = response.json()

    if response.ok is False:
        headers = dict(response.headers)
        raise ValoAPIException(
            ErrorResponse.from_dict(headers=headers, **response_data)
        )

    if version == "v1":
        return StoreFeaturedV1.from_dict(**response_data["data"])
    else:
        return [BundleV2.from_dict(**Bundles) for Bundles in response_data["data"]]
