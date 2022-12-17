from typing import List

import msgspec.json

from valo_api.endpoints_config import EndpointsConfig
from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.error_response import ErrorResponse
from valo_api.responses.website import WebsiteBannerV1
from valo_api.utils.fetch_endpoint import fetch_endpoint, response_type


def get_website_v1(countrycode: str, **kwargs) -> List[WebsiteBannerV1]:
    """Get the website banners using version 1 of the endpoint.

    This is the same as
    :py:meth:`get_website(version="v1", countrycode=countrycode, **kwargs) <get_website>`

    Args:
        countrycode: The country code to get the website banners for.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        WebsiteBannerV1: Website banners fetched from the API.
    """
    return get_website("v1", countrycode, **kwargs)


def get_website(version: str, countrycode: str, **kwargs) -> List[WebsiteBannerV1]:
    """Get the website banners using a specific version of the endpoint.

    Args:
        version: The version of the endpoint to use.
            One of the following:
            v1 (Version 1)
        countrycode: The country code to get the website banners for.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        WebsiteBannerV1: Website banners fetched from the API.

    Raises:
        ValoAPIException: If the request failed.
    """
    response = fetch_endpoint(
        EndpointsConfig.WEBSITE,
        version=version,
        countrycode=countrycode,
        **kwargs,
    )

    if response.ok is False:
        error = msgspec.json.decode(response.content, type=ErrorResponse)
        error.headers = dict(response.headers)
        raise ValoAPIException(error)

    return msgspec.json.decode(
        response.content, type=response_type(List[WebsiteBannerV1])
    ).data


try:

    from valo_api.utils.fetch_endpoint import fetch_endpoint_async

    async def get_website_v1_async(countrycode: str, **kwargs) -> List[WebsiteBannerV1]:
        """Get the website banners using version 1 of the endpoint.

        This is the same as
        :py:meth:`get_website_async(version="v1", countrycode=countrycode, **kwargs) <get_website_async>`

        Args:
            countrycode: The country code to get the website banners for.
            **kwargs: Any additional arguments to pass to the endpoint.

        Returns:
            WebsiteBannerV1: Website banners fetched from the API.
        """
        return await get_website_async("v1", countrycode, **kwargs)

    async def get_website_async(
        version: str, countrycode: str, **kwargs
    ) -> List[WebsiteBannerV1]:
        """Get the website banners using a specific version of the endpoint.

        Args:
            version: The version of the endpoint to use.
                One of the following:
                v1 (Version 1)
            countrycode: The country code to get the website banners for.
            **kwargs: Any additional arguments to pass to the endpoint.

        Returns:
            WebsiteBannerV1: Website banners fetched from the API.

        Raises:
            ValoAPIException: If the request failed.
        """
        response, content = await fetch_endpoint_async(
            EndpointsConfig.WEBSITE,
            version=version,
            countrycode=countrycode,
            **kwargs,
        )

        if response.ok is False:
            error = msgspec.json.decode(content, type=ErrorResponse)
            error.headers = dict(response.headers)
            raise ValoAPIException(error)

        return msgspec.json.decode(
            content, type=response_type(List[WebsiteBannerV1])
        ).data

except ImportError:
    pass
