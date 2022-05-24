from typing import Optional, Union

from valo_api.endpoints_config import EndpointsConfig
from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.error_response import ErrorResponse
from valo_api.responses.mmr_details import MMRDetailsV1, MMRDetailsV2, SeasonDataV2
from valo_api.utils.fetch_endpoint import fetch_endpoint


def get_mmr_details_by_puuid_v1(
    region: str, puuid: str, **kwargs
) -> Union[MMRDetailsV1, ErrorResponse]:
    return get_mmr_details_by_puuid("v1", region, puuid, **kwargs)


def get_mmr_details_by_puuid_v2(
    region: str, puuid: str, filter: Optional[str] = None, **kwargs
) -> Union[MMRDetailsV2, SeasonDataV2, ErrorResponse]:
    return get_mmr_details_by_puuid("v2", region, puuid, filter, **kwargs)


def get_mmr_details_by_name_v1(
    region: str, name: str, tag: str, **kwargs
) -> Union[MMRDetailsV1, ErrorResponse]:
    return get_mmr_details_by_name("v1", region, name, tag, **kwargs)


def get_mmr_details_by_name_v2(
    region: str, name: str, tag: str, filter: Optional[str] = None, **kwargs
) -> Union[MMRDetailsV2, SeasonDataV2, ErrorResponse]:
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
        region=region,
        name=name,
        tag=tag,
        version=version,
        query_args={"filter": str(filter).lower()} if filter is not None else None,
        **kwargs,
    )
    response_data = response.json()

    if response.ok is False:
        raise ValoAPIException(ErrorResponse.from_dict(**response_data))

    if version == "v1":
        return MMRDetailsV1.from_dict(**response_data["data"])
    elif version == "v2":
        try:
            if filter is None or filter == "":
                return MMRDetailsV2.from_dict(**response_data["data"])
            else:
                return SeasonDataV2.from_dict(**response_data["data"])
        except Exception:
            return MMRDetailsV2.from_dict(**response_data["data"])
    else:
        raise ValueError("Invalid version")


def get_mmr_details_by_puuid(
    version: str, region: str, puuid: str, filter: Optional[str] = None, **kwargs
) -> Union[MMRDetailsV1, MMRDetailsV2, SeasonDataV2, ErrorResponse]:
    response = fetch_endpoint(
        EndpointsConfig.MMR_DETAILS_BY_PUUID,
        region=region,
        puuid=puuid,
        version=version,
        query_args={"filter": str(filter).lower()} if filter is not None else None,
        **kwargs,
    )
    response_data = response.json()

    if response.ok is False:
        raise ValoAPIException(ErrorResponse.from_dict(**response_data))

    if version == "v1":
        cls = MMRDetailsV1
    elif version == "v2":
        try:
            if filter is None or filter == "":
                return MMRDetailsV2.from_dict(**response_data["data"])
            else:
                return SeasonDataV2.from_dict(**response_data["data"])
        except Exception:
            return MMRDetailsV2.from_dict(**response_data["data"])
    else:
        raise ValueError("Invalid version")

    return cls.from_dict(**response_data["data"])
