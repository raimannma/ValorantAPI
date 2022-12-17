import msgspec.json

from valo_api.endpoints_config import EndpointsConfig
from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.account_details import AccountDetailsV1
from valo_api.responses.error_response import ErrorResponse
from valo_api.utils.fetch_endpoint import fetch_endpoint, response_type


def get_account_details_by_name_v1(
    name: str, tag: str, force_update: bool = False, **kwargs
) -> AccountDetailsV1:
    """Get the account details by name for a player using version 1 of the endpoint.

    This is the same as
    :py:meth:`get_account_details_by_name(version="v1", name=name, tag=tag, force_update=force_update, **kwargs) <get_account_details>`

    Args:
        name: The name of the player to get the account details for.
        tag: The tag of the player to get the account details for.
        force_update: Whether to force an update of the account details.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        AccountDetailsV1: Account details fetched from the API.
    """
    return get_account_details_by_name("v1", name, tag, force_update, **kwargs)


def get_account_details_by_puuid_v1(
    puuid: str, force_update: bool = False, **kwargs
) -> AccountDetailsV1:
    """Get the account details for a player using version 1 of the endpoint.

    This is the same as
    :py:meth:`get_account_details_by_puuid(version="v1", puuid=puuid, force_update=force_update, **kwargs) <get_account_details_by_puuid>`

    Args:
        puuid: The puuid of the player to get the account details for.
        force_update: Whether to force an update of the account details.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        AccountDetailsV1: Account details fetched from the API.
    """
    return get_account_details_by_puuid("v1", puuid, force_update, **kwargs)


def get_account_details_by_name(
    version: str, name: str, tag: str, force_update: bool = False, **kwargs
) -> AccountDetailsV1:
    """Get the account details by name for a player using a specific version of the endpoint.

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

    if response.ok is False:
        error = msgspec.json.decode(response.content, type=ErrorResponse)
        error.headers = dict(response.headers)
        raise ValoAPIException(error)

    return msgspec.json.decode(
        response.content, type=response_type(AccountDetailsV1)
    ).data


def get_account_details_by_puuid(
    version: str, puuid: str, force_update: bool = False, **kwargs
) -> AccountDetailsV1:
    """Get the account details for a player using a specific version of the endpoint.

    Args:
        version: The version of the endpoint to use.
            One of the following:
            v1 (Version 1)
        puuid: The puuid of the player to get the account details for.
        force_update: Whether to force an update of the account details.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        AccountDetailsV1: Account details fetched from the API.

    Raises:
        ValoAPIException: If the request failed.
    """
    response = fetch_endpoint(
        EndpointsConfig.ACCOUNT_BY_PUUID,
        version=version,
        puuid=puuid,
        query_args={"force": str(force_update).lower()},
        **kwargs,
    )

    if response.ok is False:
        error = msgspec.json.decode(response.content, type=ErrorResponse)
        error.headers = dict(response.headers)
        raise ValoAPIException(error)

    return msgspec.json.decode(
        response.content, type=response_type(AccountDetailsV1)
    ).data


try:

    from valo_api.utils.fetch_endpoint import fetch_endpoint_async

    async def get_account_details_by_name_v1_async(
        name: str, tag: str, force_update: bool = False, **kwargs
    ) -> AccountDetailsV1:
        """Get the account details by name for a player using version 1 of the endpoint.

        This is the same as
        :py:meth:`get_account_details_by_name_async(version="v1", name=name, tag=tag, force_update=force_update, **kwargs) <get_account_details_by_name_async>`

        Args:
            name: The name of the player to get the account details for.
            tag: The tag of the player to get the account details for.
            force_update: Whether to force an update of the account details.
            **kwargs: Any additional arguments to pass to the endpoint.

        Returns:
            AccountDetailsV1: Account details fetched from the API.
        """
        return await get_account_details_by_name_async(
            "v1", name, tag, force_update, **kwargs
        )

    async def get_account_details_by_puuid_v1_async(
        puuid: str, force_update: bool = False, **kwargs
    ):
        """Get the account details for a player using version 1 of the endpoint.

        This is the same as
        :py:meth:`get_account_details_by_puuid_async(version="v1", puuid=puuid, force_update=force_update, **kwargs) <get_account_details_by_puuid_async>`

        Args:
            puuid: The puuid of the player to get the account details for.
            force_update: Whether to force an update of the account details.
            **kwargs: Any additional arguments to pass to the endpoint.

        Returns:
            AccountDetailsV1: Account details fetched from the API.
        """
        return await get_account_details_by_puuid_async(
            "v1", puuid, force_update, **kwargs
        )

    async def get_account_details_by_name_async(
        version: str, name: str, tag: str, force_update: bool = False, **kwargs
    ) -> AccountDetailsV1:
        """Get the account details by name for a player using a specific version of the endpoint.

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
        response, content = await fetch_endpoint_async(
            EndpointsConfig.ACCOUNT_BY_NAME,
            version=version,
            name=name,
            tag=tag,
            query_args={"force": str(force_update).lower()},
            **kwargs,
        )

        if response.ok is False:
            error = msgspec.json.decode(content, type=ErrorResponse)
            error.headers = dict(response.headers)
            raise ValoAPIException(error)

        return msgspec.json.decode(content, type=response_type(AccountDetailsV1)).data

    async def get_account_details_by_puuid_async(
        version: str, puuid: str, force_update: bool = False, **kwargs
    ) -> AccountDetailsV1:
        """Get the account details for a player using a specific version of the endpoint.

        Args:
            version: The version of the endpoint to use.
                One of the following:
                v1 (Version 1)
            puuid: The puuid of the player to get the account details for.
            force_update: Whether to force an update of the account details.
            **kwargs: Any additional arguments to pass to the endpoint.

        Returns:
            AccountDetailsV1: Account details fetched from the API.

        Raises:
            ValoAPIException: If the request failed.
        """
        response, content = await fetch_endpoint_async(
            EndpointsConfig.ACCOUNT_BY_PUUID,
            version=version,
            puuid=puuid,
            query_args={"force": str(force_update).lower()},
            **kwargs,
        )

        if response.ok is False:
            error = msgspec.json.decode(content, type=ErrorResponse)
            error.headers = dict(response.headers)
            raise ValoAPIException(error)

        return msgspec.json.decode(content, type=response_type(AccountDetailsV1)).data

except ImportError as e:
    pass
