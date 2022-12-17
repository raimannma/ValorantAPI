from typing import List, Union

import msgspec.json

from valo_api.endpoints_config import EndpointsConfig
from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.error_response import ErrorResponse
from valo_api.responses.store_featured import BundleV2, StoreFeaturedV1
from valo_api.utils.fetch_endpoint import fetch_endpoint, response_type


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

    if response.ok is False:
        error = msgspec.json.decode(response.content, type=ErrorResponse)
        error.headers = dict(response.headers)
        raise ValoAPIException(error)

    if version == "v1":
        return msgspec.json.decode(
            response.content, type=response_type(StoreFeaturedV1)
        ).data
    else:
        return msgspec.json.decode(
            response.content, type=response_type(List[BundleV2])
        ).data


try:

    from valo_api.utils.fetch_endpoint import fetch_endpoint_async

    async def get_store_featured_v1_async(**kwargs) -> StoreFeaturedV1:
        """Get the store featured using version 1 of the endpoint.

        This is the same as
        :py:meth:`get_store_featured_async(version="v1", **kwargs) <get_store_featured_async>`

        Args:
            **kwargs: Any additional arguments to pass to the endpoint.

        Returns:
            StoreFeaturedV1: Store featured fetched from the API.
        """
        return await get_store_featured_async("v1", **kwargs)

    async def get_store_featured_v2_async(**kwargs) -> List[BundleV2]:
        """Get the store featured using version 2 of the endpoint.

        This is the same as
        :py:meth:`get_store_featured_async(version="v2", **kwargs) <get_store_featured_async>`

        Args:
            **kwargs: Any additional arguments to pass to the endpoint.

        Returns:
            List[BundleV2]: Bundles featured fetched from the API.
        """
        return await get_store_featured_async("v2", **kwargs)

    async def get_store_featured_async(
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
        response, content = await fetch_endpoint_async(
            EndpointsConfig.STORE_FEATURED,
            version=version,
            **kwargs,
        )

        if response.ok is False:
            error = msgspec.json.decode(content, type=ErrorResponse)
            error.headers = dict(response.headers)
            raise ValoAPIException(error)

        if version == "v1":
            return msgspec.json.decode(
                content, type=response_type(StoreFeaturedV1)
            ).data
        else:
            return msgspec.json.decode(content, type=response_type(List[BundleV2])).data

except ImportError:
    pass
