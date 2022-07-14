from valo_api.endpoints_config import EndpointsConfig
from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.account_details import AccountDetailsV1
from valo_api.responses.error_response import ErrorResponse
from valo_api.utils.fetch_endpoint import fetch_endpoint


def get_account_details_v1(
    name: str, tag: str, force_update: bool = False, **kwargs
) -> AccountDetailsV1:
    """Get the account details for a player using version 1 of the endpoint.

    This is the same as
    :py:meth:`get_account_details(version="v1", name=name, tag=tag, force_update=force_update, **kwargs) <get_account_details>`

    Args:
        name: The name of the player to get the account details for.
        tag: The tag of the player to get the account details for.
        force_update: Whether to force an update of the account details.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        AccountDetailsV1: Account details fetched from the API.
    """
    return get_account_details("v1", name, tag, force_update, **kwargs)


def get_account_details(
    version: str, name: str, tag: str, force_update: bool = False, **kwargs
) -> AccountDetailsV1:
    """Get the account details for a player using a specific version of the endpoint.

    Args:
        version: The version of the endpoint to use.
            One of the following:
            v1 (Version 1)
        name: The name of the player to get the account details for.
        tag: The tag of the player to get the account details for.
        force_update: Whether to force an update of the account details.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        AccountDetailsV1: Account details fetched from the API.

    Raises:
        ValoAPIException: If the request failed.
    """
    response = fetch_endpoint(
        EndpointsConfig.ACCOUNT_BY_NAME,
        version=version,
        name=name,
        tag=tag,
        query_args={"force": str(force_update).lower()},
        **kwargs,
    )
    response_data = response.json()

    if response.ok is False:
        headers = dict(response.headers)
        raise ValoAPIException(
            ErrorResponse.from_dict(headers=headers, **response_data)
        )

    return AccountDetailsV1.from_dict(**response_data["data"])
