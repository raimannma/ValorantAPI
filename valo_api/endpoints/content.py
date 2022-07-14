from typing import Optional

from valo_api.endpoints_config import EndpointsConfig
from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.content import ContentV1
from valo_api.responses.error_response import ErrorResponse
from valo_api.utils.fetch_endpoint import fetch_endpoint


def get_content_v1(locale: Optional[str] = None, **kwargs) -> ContentV1:
    """Get the content for a specific locale using version 1 of the endpoint.

    This is the same as
    :py:meth:`get_content(version="v1", locale=locale, **kwargs) <get_content>`

    Args:
        locale: The locale to get the content for.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        ContentV1: Content fetched from the API.
    """
    return get_content("v1", locale, **kwargs)


def get_content(version: str, locale: Optional[str] = None, **kwargs) -> ContentV1:
    """Get the content for a specific locale using a specific version of the endpoint.

    Args:
        version: The version of the endpoint to use.
            One of the following:
            v1 (Version 1)
        locale: The locale to get the content for.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        ContentV1: Content fetched from the API.

    Raises:
        ValoAPIException: If the request failed.
    """
    response = fetch_endpoint(
        EndpointsConfig.CONTENT,
        version=version,
        query_args={"locale": str(locale).lower()} if locale else None,
        **kwargs,
    )
    response_data = response.json()

    if response.ok is False:
        headers = dict(response.headers)
        raise ValoAPIException(
            ErrorResponse.from_dict(headers=headers, **response_data)
        )

    return ContentV1.from_dict(**response_data)
