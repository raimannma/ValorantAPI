from valo_api.endpoints_config import EndpointsConfig
from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.error_response import ErrorResponse
from valo_api.responses.status import StatusV1
from valo_api.utils.fetch_endpoint import fetch_endpoint


def get_status_v1(region: str, **kwargs) -> StatusV1:
    """Get the status for a specific region using version 1 of the endpoint.

    This is the same as
    :py:meth:`get_status(version="v1", region=region, **kwargs) <get_status>`

    Args:
        region: The region to get the status for.
            One of the following:
            eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        StatusV1: Status fetched from the API.
    """
    return get_status("v1", region, **kwargs)


def get_status(version: str, region: str, **kwargs) -> StatusV1:
    """Get the status for a specific region.

    Args:
        version: The version of the endpoint to use.
            One of the following:
            v1 (Version 1)
        region: The region to get the status for.
            One of the following:
            eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        StatusV1: Status fetched from the API.

    Raises:
        ValoAPIException: If the request failed.
    """
    response = fetch_endpoint(
        EndpointsConfig.STATUS,
        version=version,
        region=region,
        **kwargs,
    )
    response_data = response.json()

    if response.ok is False:
        headers = dict(response.headers)
        raise ValoAPIException(
            ErrorResponse.from_dict(headers=headers, **response_data)
        )

    return StatusV1.from_dict(**response_data["data"])
