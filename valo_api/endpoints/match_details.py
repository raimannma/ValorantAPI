import msgspec.json

from valo_api.endpoints_config import EndpointsConfig
from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.error_response import ErrorResponse
from valo_api.responses.match_history import MatchHistoryPointV3
from valo_api.utils.fetch_endpoint import fetch_endpoint, response_type


def get_match_details_v2(match_id: str, **kwargs) -> MatchHistoryPointV3:
    """Get the match details for a match using version 2 of the endpoint.

    This is the same as
    :py:meth:`get_match_details(version="v2", match_id=match_id, **kwargs) <get_match_details>`

    Args:
        match_id: The match ID to get the details for.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        MatchHistoryPointV3: Match details fetched from the API.
    """
    return get_match_details("v2", match_id, **kwargs)


def get_match_details(version: str, match_id: str, **kwargs) -> MatchHistoryPointV3:
    """Get the match details for a match using a specific version of the endpoint.

    Args:
        version: The version of the endpoint to use.
            One of the following:
            v2 (Version 2)
        match_id: The match ID to get the details for.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        MatchHistoryPointV3: Match details fetched from the API.

    Raises:
        ValoAPIException: If the request failed.
    """
    response = fetch_endpoint(
        EndpointsConfig.MATCH_DETAILS,
        version=version,
        match_id=match_id,
        **kwargs,
    )

    if response.ok is False:
        error = msgspec.json.decode(response.content, type=ErrorResponse)
        error.headers = dict(response.headers)
        raise ValoAPIException(error)

    return msgspec.json.decode(
        response.content, type=response_type(MatchHistoryPointV3)
    ).data


try:

    from valo_api.utils.fetch_endpoint import fetch_endpoint_async

    async def get_match_details_v2_async(
        match_id: str, **kwargs
    ) -> MatchHistoryPointV3:
        """Get the match details for a match using version 2 of the endpoint.

        This is the same as
        :py:meth:`get_match_details_async(version="v2", match_id=match_id, **kwargs) <get_match_details_async>`

        Args:
            match_id: The match ID to get the details for.
            **kwargs: Any additional arguments to pass to the endpoint.

        Returns:
            MatchHistoryPointV3: Match details fetched from the API.
        """
        return await get_match_details_async("v2", match_id, **kwargs)

    async def get_match_details_async(
        version: str, match_id: str, **kwargs
    ) -> MatchHistoryPointV3:
        """Get the match details for a match using a specific version of the endpoint.

        Args:
            version: The version of the endpoint to use.
                One of the following:
                v2 (Version 2)
            match_id: The match ID to get the details for.
            **kwargs: Any additional arguments to pass to the endpoint.

        Returns:
            MatchHistoryPointV3: Match details fetched from the API.

        Raises:
            ValoAPIException: If the request failed.
        """
        response, content = await fetch_endpoint_async(
            EndpointsConfig.MATCH_DETAILS,
            version=version,
            match_id=match_id,
            **kwargs,
        )

        if response.ok is False:
            error = msgspec.json.decode(content, type=ErrorResponse)
            error.headers = dict(response.headers)
            raise ValoAPIException(error)

        return msgspec.json.decode(
            content, type=response_type(MatchHistoryPointV3)
        ).data

except ImportError:
    pass
