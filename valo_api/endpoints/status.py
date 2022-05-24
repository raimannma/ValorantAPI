from typing import Union

from valo_api.endpoints_config import EndpointsConfig
from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.error_response import ErrorResponse
from valo_api.responses.status import StatusV1
from valo_api.utils.fetch_endpoint import fetch_endpoint


def get_status_v1(region: str, **kwargs) -> Union[StatusV1, ErrorResponse]:
    return get_status("v1", region, **kwargs)


def get_status(version: str, region: str, **kwargs) -> Union[StatusV1, ErrorResponse]:
    response = fetch_endpoint(
        EndpointsConfig.STATUS,
        version=version,
        region=region,
        **kwargs,
    )
    response_data = response.json()

    if response.ok is False:
        raise ValoAPIException(ErrorResponse.from_dict(**response_data))

    return StatusV1.from_dict(**response_data["data"])
