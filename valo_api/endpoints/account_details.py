from typing import Union

from valo_api.endpoints_config import EndpointsConfig
from valo_api.responses.account_details import AccountDetailsV1
from valo_api.responses.error_response import ErrorResponse
from valo_api.utils.fetch_endpoint import fetch_endpoint


def get_account_details_v1(
    name: str, tag: str, force_update: bool = False, **kwargs
) -> Union[AccountDetailsV1, ErrorResponse]:
    return get_account_details("v1", name, tag, force_update, **kwargs)


def get_account_details(
    version: str, name: str, tag: str, force_update: bool = False, **kwargs
) -> Union[AccountDetailsV1, ErrorResponse]:
    response = fetch_endpoint(
        EndpointsConfig.ACCOUNT_BY_NAME,
        {"force": str(force_update).lower()},
        version=version,
        name=name,
        tag=tag,
        **kwargs,
    )
    response_data = response.json()

    if response.ok is False:
        return ErrorResponse.from_dict(**response_data)

    return AccountDetailsV1.from_dict(**response_data["data"])
