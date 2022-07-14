from typing import List

from valo_api.endpoints_config import EndpointsConfig
from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.error_response import ErrorResponse
from valo_api.responses.website import WebsiteBannerV1
from valo_api.utils.fetch_endpoint import fetch_endpoint


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
    response_data = response.json()

    if response.ok is False:
        headers = dict(response.headers)
        raise ValoAPIException(
            ErrorResponse.from_dict(headers=headers, **response_data)
        )

    return [WebsiteBannerV1.from_dict(**banner) for banner in response_data["data"]]
