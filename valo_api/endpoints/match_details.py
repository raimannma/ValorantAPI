from valo_api.endpoints_config import EndpointsConfig
from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.error_response import ErrorResponse
from valo_api.responses.match_history import MatchHistoryPointV3
from valo_api.utils.fetch_endpoint import fetch_endpoint


def get_match_details_v2(matchId: str, **kwargs) -> MatchHistoryPointV3:
    """Get the match details for a match using version 2 of the endpoint.

    This is the same as
    :py:meth:`get_match_details(version="v2", matchId=matchId, **kwargs) <get_match_details>`

    Args:
        matchId: The match ID to get the details for.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        MatchHistoryPointV3: Match details fetched from the API.
    """
    return get_match_details("v2", matchId, **kwargs)


def get_match_details(version: str, matchId: str, **kwargs) -> MatchHistoryPointV3:
    """Get the match details for a match using a specific version of the endpoint.

    Args:
        version: The version of the endpoint to use.
            One of the following:
            v2 (Version 2)
        matchId: The match ID to get the details for.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        MatchHistoryPointV3: Match details fetched from the API.

    Raises:
        ValoAPIException: If the request failed.
    """
    response = fetch_endpoint(
        EndpointsConfig.MATCH_DETAILS,
        version=version,
        matchId=matchId,
        **kwargs,
    )
    response_data = response.json()

    if response.ok is False:
        headers = dict(response.headers)
        raise ValoAPIException(
            ErrorResponse.from_dict(headers=headers, **response_data)
        )

    return MatchHistoryPointV3.from_dict(**response_data["data"])
