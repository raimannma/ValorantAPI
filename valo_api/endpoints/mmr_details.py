from typing import Optional, Union

from valo_api.endpoints_config import EndpointsConfig
from valo_api.responses.error_response import ErrorResponse
from valo_api.responses.mmr_details import MMRDetailsV1, MMRDetailsV2, SeasonDataV2
from valo_api.utils.fetch_endpoint import fetch_endpoint


def get_mmr_details_by_puuid_v1(
    region: str, puuid: str, **kwargs
) -> Union[MMRDetailsV1, ErrorResponse]:
    return get_mmr_details_by_puuid("v1", region, puuid, **kwargs)


def get_mmr_details_by_puuid_v2(
    region: str, puuid: str, filter: Optional[str] = None, **kwargs
) -> Union[MMRDetailsV2, ErrorResponse]:
    return get_mmr_details_by_puuid("v2", region, puuid, filter, **kwargs)


def get_mmr_details_by_name_v1(
    region: str, name: str, tag: str, **kwargs
) -> Union[MMRDetailsV1, ErrorResponse]:
    return get_mmr_details_by_name("v1", region, name, tag, **kwargs)


def get_mmr_details_by_name_v2(
    region: str, name: str, tag: str, filter: Optional[str] = None, **kwargs
) -> Union[MMRDetailsV2, ErrorResponse]:
    return get_mmr_details_by_name("v2", region, name, tag, filter, **kwargs)


def get_mmr_details_by_name(
    version: str,
    region: str,
    name: str,
    tag: str,
    filter: Optional[str] = None,
    **kwargs,
) -> Union[MMRDetailsV1, MMRDetailsV2, SeasonDataV2, ErrorResponse]:
    response = fetch_endpoint(
        EndpointsConfig.MMR_DETAILS_BY_NAME,
        {"filter": filter} if filter else {},
        region=region,
        name=name,
        tag=tag,
        version=version,
        **kwargs,
    )
    response_data = response.json()

    if response.ok is False:
        try:
            return ErrorResponse.from_dict(**response_data)
        except Exception:
            raise Exception(response_data)

    if version == "v1":
        cls = MMRDetailsV1
    elif version == "v2":
        if filter is None:
            cls = MMRDetailsV2
        else:
            cls = SeasonDataV2
    else:
        raise ValueError("Invalid version")

    return cls.from_dict(**response_data["data"])


def get_mmr_details_by_puuid(
    version: str, region: str, puuid: str, filter: Optional[str] = None, **kwargs
) -> Union[MMRDetailsV1, MMRDetailsV2, SeasonDataV2, ErrorResponse]:
    response = fetch_endpoint(
        EndpointsConfig.MMR_DETAILS_BY_PUUID,
        {"filter": filter} if filter else {},
        region=region,
        puuid=puuid,
        version=version,
        **kwargs,
    )
    response_data = response.json()

    if response.ok is False:
        try:
            return ErrorResponse.from_dict(**response_data)
        except Exception:
            raise Exception(response_data)

    if version == "v1":
        cls = MMRDetailsV1
    elif version == "v2":
        if filter is None:
            cls = MMRDetailsV2
        else:
            cls = SeasonDataV2
    else:
        raise ValueError("Invalid version")

    return cls.from_dict(**response_data["data"])
