from typing import List, Union

from valo_api.endpoints_config import EndpointsConfig
from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.error_response import ErrorResponse
from valo_api.responses.mmr_history import MMRHistoryPointV1
from valo_api.utils.fetch_endpoint import fetch_endpoint


def get_mmr_history_by_name_v1(
    region: str, name: str, tag: str, **kwargs
) -> Union[List[MMRHistoryPointV1], ErrorResponse]:
    return get_mmr_history_by_name("v1", region, name, tag, **kwargs)


def get_mmr_history_by_puuid_v1(
    region: str, puuid: str, **kwargs
) -> Union[List[MMRHistoryPointV1], ErrorResponse]:
    return get_mmr_history_by_puuid("v1", region, puuid, **kwargs)


def get_mmr_history_by_name(
    version: str, region: str, name: str, tag: str, **kwargs
) -> Union[List[MMRHistoryPointV1], ErrorResponse]:
    response = fetch_endpoint(
        EndpointsConfig.MMR_HISTORY_BY_NAME,
        region=region,
        name=name,
        tag=tag,
        version=version,
        **kwargs,
    )
    response_data = response.json()

    if response.ok is False:
        raise ValoAPIException(ErrorResponse.from_dict(**response_data))

    return [MMRHistoryPointV1.from_dict(**point) for point in response_data["data"]]


def get_mmr_history_by_puuid(
    version: str, region: str, puuid: str, **kwargs
) -> Union[List[MMRHistoryPointV1], ErrorResponse]:
    response = fetch_endpoint(
        EndpointsConfig.MMR_HISTORY_BY_PUUID,
        region=region,
        puuid=puuid,
        version=version,
        **kwargs,
    )
    response_data = response.json()

    if response.ok is False:
        raise ValoAPIException(ErrorResponse.from_dict(**response_data))

    return [MMRHistoryPointV1.from_dict(**point) for point in response_data["data"]]
