from typing import Union

from valo_api.endpoints_config import EndpointsConfig
from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.error_response import ErrorResponse
from valo_api.responses.store_offers import StoreOffersV1
from valo_api.utils.fetch_endpoint import fetch_endpoint


def get_store_offers_v1(**kwargs) -> Union[StoreOffersV1, ErrorResponse]:
    return get_store_offers("v1", **kwargs)


def get_store_offers(version: str, **kwargs) -> Union[StoreOffersV1, ErrorResponse]:
    response = fetch_endpoint(
        EndpointsConfig.STORE_OFFERS,
        version=version,
        **kwargs,
    )
    response_data = response.json()

    if response.ok is False:
        raise ValoAPIException(ErrorResponse.from_dict(**response_data))

    return StoreOffersV1.from_dict(**response_data["data"])
