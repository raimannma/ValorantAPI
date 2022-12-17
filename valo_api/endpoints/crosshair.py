import io

import msgspec.json
from PIL import Image

from valo_api.endpoints_config import EndpointsConfig
from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.error_response import ErrorResponse
from valo_api.utils.fetch_endpoint import fetch_endpoint


def get_crosshair_v1(crosshair_id: str, **kwargs) -> Image.Image:
    """Get an image of the crosshair using the v1 endpoint.

    This is the same as
    :py:meth:`get_crosshair(version="v1", id=id, **kwargs) <get_crosshair>`

    Args:
        crosshair_id: The crosshair ID to get the image for.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        Image: An image object containing the crosshair image.
    """
    return get_crosshair("v1", crosshair_id, **kwargs)


def get_crosshair(version: str, crosshair_id: str, **kwargs) -> Image.Image:
    """Get an image of the crosshair using the specified endpoint.

    Args:
        version: The version of the endpoint to use.
            One of the following:
            v1 (Version 1)
        crosshair_id: The crosshair ID to get the image for.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        Image: An image object containing the crosshair image.

    Raises:
        ValoAPIException: If the request failed.
    """
    response = fetch_endpoint(
        EndpointsConfig.CROSSHAIR,
        version=version,
        query_args={"id": crosshair_id},
        **kwargs,
    )

    if response.ok is False:
        error = msgspec.json.decode(response.content, type=ErrorResponse)
        error.headers = dict(response.headers)
        raise ValoAPIException(error)

    return Image.open(io.BytesIO(response.content))


try:
    from valo_api.utils.fetch_endpoint import fetch_endpoint_async

    async def get_crosshair_v1_async(crosshair_id: str, **kwargs) -> Image.Image:
        """Get an image of the crosshair using the v1 endpoint.

        This is the same as
        :py:meth:`get_crosshair_async(version="v1", id=id, **kwargs) <get_crosshair_async>`

        Args:
            crosshair_id: The crosshair ID to get the image for.
            **kwargs: Any additional arguments to pass to the endpoint.

        Returns:
            Image: An image object containing the crosshair image.
        """
        return await get_crosshair_async("v1", crosshair_id, **kwargs)

    async def get_crosshair_async(
        version: str, crosshair_id: str, **kwargs
    ) -> Image.Image:
        """Get an image of the crosshair using the specified endpoint.

        Args:
            version: The version of the endpoint to use.
                One of the following:
                v1 (Version 1)
            crosshair_id: The crosshair ID to get the image for.
            **kwargs: Any additional arguments to pass to the endpoint.

        Returns:
            Image: An image object containing the crosshair image.

        Raises:
            ValoAPIException: If the request failed.
        """
        response, content = await fetch_endpoint_async(
            EndpointsConfig.CROSSHAIR,
            version=version,
            query_args={"id": crosshair_id},
            **kwargs,
        )

        if response.ok is False:
            error = msgspec.json.decode(content, type=ErrorResponse)
            error.headers = dict(response.headers)
            raise ValoAPIException(error)

        return Image.open(io.BytesIO(content))

except ImportError:
    pass
