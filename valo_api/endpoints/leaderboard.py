from typing import List, Union

from valo_api.endpoints_config import EndpointsConfig
from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.error_response import ErrorResponse
from valo_api.responses.leaderboard import LeaderboardPlayerV1, LeaderboardV2
from valo_api.utils.fetch_endpoint import fetch_endpoint


def get_leaderboard_v1(
    region: str, **kwargs
) -> Union[List[LeaderboardPlayerV1], ErrorResponse]:
    return get_leaderboard("v1", region, **kwargs)


def get_leaderboard_v2(region: str, **kwargs) -> Union[LeaderboardV2, ErrorResponse]:
    return get_leaderboard("v2", region, **kwargs)


def get_leaderboard(
    version: str, region: str, **kwargs
) -> Union[LeaderboardV2, List[LeaderboardPlayerV1], ErrorResponse]:
    response = fetch_endpoint(
        EndpointsConfig.LEADERBOARD,
        region=region,
        version=version,
        **kwargs,
    )
    response_data = response.json()

    if response.ok is False:
        raise ValoAPIException(ErrorResponse.from_dict(**response_data))

    if version == "v1":
        return [LeaderboardPlayerV1.from_dict(**player) for player in response_data]
    else:
        return LeaderboardV2.from_dict(**response_data)
