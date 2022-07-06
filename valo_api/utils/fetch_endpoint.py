from typing import Any, Dict, Optional

import os
import urllib.parse

import requests
from requests import Response

from valo_api.config import Config


def encode_params(**kwargs) -> Dict[str, str]:
    """Returns a string of the parameters to be used in a URL.

    Args:
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        A dictionary of the parameters to be used in a URL.
    """
    out = dict()
    for key, value in kwargs.items():
        encoded_key = urllib.parse.quote_plus(str(key))
        encoded_value = urllib.parse.quote_plus(str(value))
        out[encoded_key] = encoded_value
    return out


def fetch_endpoint(
    endpoint_definition: str,
    query_args: Optional[Dict[str, Any]] = None,
    method: str = "GET",
    **kwargs,
) -> Response:
    """Fetches an endpoint from the API.

    Args:
        endpoint_definition: The endpoint definition to use.
        query_args: Any additional arguments to pass to the endpoint.
        method: The method to use when fetching the endpoint.
        **kwargs: Any additional arguments to pass to the endpoint.

    Returns:
        A response from the API.
    """
    endpoint_definition = endpoint_definition.lower()
    encoded_params = encode_params(**kwargs)

    # Build the URL
    # First Replace the parameters in the endpoint definition
    for key, value in encoded_params.items():
        endpoint_definition = endpoint_definition.replace(
            f"{{{key.lower()}}}", value.lower()
        )

    # Then add the base URL
    url = f"{Config.BASE_URL}{endpoint_definition}"

    # Set the headers
    headers = {
        "User-Agent": Config.USER_AGENT,
        "Accept": "application/json",
    }
    if "VALO_API_KEY" in os.environ and os.environ["VALO_API_KEY"] is not None:
        headers["Authorization"] = os.environ["VALO_API_KEY"]

    # Make the request
    return requests.request(
        method, url, params=query_args, json=query_args, headers=headers
    )
