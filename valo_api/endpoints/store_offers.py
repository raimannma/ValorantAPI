import msgspec.json

from valo_api.endpoints_config import EndpointsConfig
from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.error_response import ErrorResponse
from valo_api.responses.store_offers import StoreOffersV1
from valo_api.utils.fetch_endpoint import fetch_endpoint, response_type


def get_store_offers_v1(**kwargs) -> StoreOffersV1:
    """Get the store offers using version 1 of the endpoint.

    This is the same as
    :py:meth:`get_store_offers(version="v1", **kwargs) <get_store_offers>`

    Args:
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        StoreOffersV1: Store Offers fetched from the API.
    """
    return get_store_offers("v1", **kwargs)


def get_store_offers(version: str, **kwargs) -> StoreOffersV1:
    """Get the store offers using a specific version of the endpoint.

    Args:
        version: The version of the endpoint to use.
            One of the following:
            v1 (Version 1)
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        StoreOffersV1: Store Offers fetched from the API.

    Raises:
        ValoAPIException: If the request failed.
    """
    response = fetch_endpoint(
        EndpointsConfig.STORE_OFFERS,
        version=version,
        **kwargs,
    )

    if response.ok is False:
        error = msgspec.json.decode(response.content, type=ErrorResponse)
        error.headers = dict(response.headers)
        raise ValoAPIException(error)

    return msgspec.json.decode(response.content, type=response_type(StoreOffersV1)).data


try:

    from valo_api.utils.fetch_endpoint import fetch_endpoint_async

    async def get_store_offers_v1_async(**kwargs) -> StoreOffersV1:
        """Get the store offers using version 1 of the endpoint.

        This is the same as
        :py:meth:`get_store_offers(version="v1", **kwargs) <get_store_offers>`

        Args:
            **kwargs: Any additional arguments to pass to the endpoint.

        Returns:
            StoreOffersV1: Store Offers fetched from the API.
        """
        return await get_store_offers_async("v1", **kwargs)

    async def get_store_offers_async(version: str, **kwargs) -> StoreOffersV1:
        """Get the store offers using a specific version of the endpoint.

        Args:
            version: The version of the endpoint to use.
                One of the following:
                v1 (Version 1)
            **kwargs: Any additional arguments to pass to the endpoint.

        Returns:
            StoreOffersV1: Store Offers fetched from the API.

        Raises:
            ValoAPIException: If the request failed.
        """
        response, content = await fetch_endpoint_async(
            EndpointsConfig.STORE_OFFERS,
            version=version,
            **kwargs,
        )

        if response.ok is False:
            error = msgspec.json.decode(content, type=ErrorResponse)
            error.headers = dict(response.headers)
            raise ValoAPIException(error)

        return msgspec.json.decode(content, type=response_type(StoreOffersV1)).data

except ImportError:
    pass
