from valo_api.endpoints_config import EndpointsConfig
from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.error_response import ErrorResponse
from valo_api.responses.version_info import VersionInfoV1
from valo_api.utils.fetch_endpoint import fetch_endpoint


def get_version_info_v1(region: str, **kwargs) -> VersionInfoV1:
    """Get the version info using version 1 of the endpoint.

    This is the same as
    :py:meth:`get_version_info(version="v1", region=region, **kwargs) <get_version_info>`

    Args:
        region: The region to get the version info for.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        VersionInfoV1: Version info fetched from the API.
    """
    return get_version_info("v1", region, **kwargs)


def get_version_info(version: str, region: str, **kwargs) -> VersionInfoV1:
    """Get the version info using a specific version of the endpoint.

    Args:
        version: The version of the endpoint to use.
            One of the following:
            v1 (Version 1)
        region: The region to get the version info for.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        VersionInfoV1: Version info fetched from the API.

    Raises:
        ValoAPIException: If the request failed.
    """
    response = fetch_endpoint(
        EndpointsConfig.VERSION_INFO,
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

    return VersionInfoV1.from_dict(**response_data["data"])
