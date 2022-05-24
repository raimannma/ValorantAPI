from typing import Optional, Union

from valo_api.endpoints_config import EndpointsConfig
from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.content import ContentV1
from valo_api.responses.error_response import ErrorResponse
from valo_api.utils.fetch_endpoint import fetch_endpoint


def get_content_v1(
    locale: Optional[str] = None, **kwargs
) -> Union[ContentV1, ErrorResponse]:
    return get_content("v1", locale, **kwargs)


def get_content(
    version: str, locale: Optional[str] = None, **kwargs
) -> Union[ContentV1, ErrorResponse]:
    response = fetch_endpoint(
        EndpointsConfig.CONTENT,
        version=version,
        query_args={"locale": str(locale).lower()} if locale else None,
        **kwargs,
    )
    response_data = response.json()

    if response.ok is False:
        raise ValoAPIException(ErrorResponse.from_dict(**response_data))

    return ContentV1.from_dict(**response_data)
