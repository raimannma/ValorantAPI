import msgspec.json

from valo_api.endpoints_config import EndpointsConfig
from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.error_response import ErrorResponse
from valo_api.responses.status import StatusV1
from valo_api.utils.fetch_endpoint import fetch_endpoint, response_type


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

    if response.ok is False:
        error = msgspec.json.decode(response.content, type=ErrorResponse)
        error.headers = dict(response.headers)
        raise ValoAPIException(error)

    return msgspec.json.decode(response.content, type=response_type(StatusV1)).data


try:

    from valo_api.utils.fetch_endpoint import fetch_endpoint_async

    async def get_status_v1_async(region: str, **kwargs) -> StatusV1:
        """Get the status for a specific region using version 1 of the endpoint.

        This is the same as
        :py:meth:`get_status_async(version="v1", region=region, **kwargs) <get_status_async>`

        Args:
            region: The region to get the status for.
                One of the following:
                eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
            **kwargs: Any additional arguments to pass to the endpoint.

        Returns:
            StatusV1: Status fetched from the API.
        """
        return await get_status_async("v1", region, **kwargs)

    async def get_status_async(version: str, region: str, **kwargs) -> StatusV1:
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
        response, content = await fetch_endpoint_async(
            EndpointsConfig.STATUS,
            version=version,
            region=region,
            **kwargs,
        )

        if response.ok is False:
            error = msgspec.json.decode(content, type=ErrorResponse)
            error.headers = dict(response.headers)
            raise ValoAPIException(error)

        return msgspec.json.decode(content, type=response_type(StatusV1)).data

except ImportError:
    pass
