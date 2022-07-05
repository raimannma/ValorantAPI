from typing import List, Optional, Union

from valo_api.endpoints_config import EndpointsConfig
from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.error_response import ErrorResponse
from valo_api.responses.leaderboard import LeaderboardPlayerV1, LeaderboardV2
from valo_api.utils.fetch_endpoint import fetch_endpoint


def get_leaderboard_v1(
    region: str,
    puuid: Optional[str] = None,
    name: Optional[str] = None,
    tag: Optional[str] = None,
    **kwargs,
) -> List[LeaderboardPlayerV1]:
    """Get the leaderboard for a region using version 1 of the endpoint.

    This is the same as
    :py:meth:`get_leaderboard(version="v1", region=region, puuid=puuid, name=name, tag=tag, **kwargs) <get_leaderboard>`

    You can also filter by puuid or name and tag.

    Args:
        region: The region to get the leaderboard for.
            One of the following:
            eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
        puuid: The puuid of the player to get the leaderboard for.
        name: The name of the player to get the leaderboard for.
        tag: The tag of the player to get the leaderboard for.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        A list of LeaderboardPlayerV1 objects.
    """
    return get_leaderboard("v1", region, puuid, name, tag, **kwargs)


def get_leaderboard_v2(region: str, **kwargs) -> LeaderboardV2:
    """Get the leaderboard for a region using version 2 of the endpoint.

    This is the same as :py:meth:`get_leaderboard(version="v2", region=region, **kwargs) <get_leaderboard>`

    Args:
        region: The region to get the leaderboard for.
            One of the following:
            eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        A LeaderboardV2 object.
    """
    return get_leaderboard("v2", region, **kwargs)


def get_leaderboard(
    version: str,
    region: str,
    puuid: Optional[str] = None,
    name: Optional[str] = None,
    tag: Optional[str] = None,
    **kwargs,
) -> Union[LeaderboardV2, List[LeaderboardPlayerV1]]:
    """Get the leaderboard for a region using a specific version of the endpoint.

    You can also filter by puuid or name and tag if you are using v1.

    Args:
        version: The version of the endpoint. One of the following:
            v1 (Version 1), v2 (Version 2)
        region: The region to get the leaderboard for.
            One of the following:
            eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
        puuid: The puuid of the player to get the leaderboard for.
        name: The name of the player to get the leaderboard for.
        tag: The tag of the player to get the leaderboard for.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        - A list of LeaderboardPlayerV1 objects if version is v1.
        - A LeaderboardV2 object if version is v2.

    Raises:
        ValoAPIException: If the request failed.
    """
    if version == "v2":
        if puuid is not None or name is not None or tag is not None:
            raise ValoAPIException("puuid, name and tag are not allowed for version v2")

    query_args = dict()
    if puuid is not None:
        query_args["puuid"] = puuid
    if name is not None:
        query_args["name"] = name
    if tag is not None:
        query_args["tag"] = tag

    response = fetch_endpoint(
        EndpointsConfig.LEADERBOARD,
        region=region,
        version=version,
        query_args=query_args,
        **kwargs,
    )
    response_data = response.json()

    if response.ok is False:
        raise ValoAPIException(ErrorResponse.from_dict(**response_data))

    if version == "v1":
        if puuid is not None or name is not None or tag is not None:
            response_data = response_data["data"]
        return [LeaderboardPlayerV1.from_dict(**player) for player in response_data]
    else:
        return LeaderboardV2.from_dict(**response_data)
