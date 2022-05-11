from typing import Any, Dict, Optional

import urllib.parse

import requests
from requests import Response

from valo_api.config import Config


def encode_params(**kwargs):
    """
    Returns a string of the parameters to be used in a URL.
    """
    out = dict()
    for key, value in kwargs.items():
        encoded_key = urllib.parse.quote_plus(str(key))
        encoded_value = urllib.parse.quote_plus(str(value))
        out[encoded_key] = encoded_value
    return out


def fetch_endpoint(
    endpoint_definition, query_args: Optional[Dict[str, Any]] = None, **kwargs
) -> Response:
    """
    Fetches an endpoint from the API.
    """
    endpoint_definition = endpoint_definition.lower()
    encoded_params = encode_params(**kwargs)

    # Build the URL
    # First Replace the parameters in the endpoint definition
    for key, value in encoded_params.items():
        endpoint_definition = endpoint_definition.replace(
            f"{{{key.lower()}}}", value.lower()
        )

    # Then add the query arguments
    if query_args is not None and len(query_args) > 0:
        endpoint_definition = (
            f"{endpoint_definition}?{urllib.parse.urlencode(query_args)}"
        )

    # Then add the base URL
    url = f"{Config.BASE_URL}{endpoint_definition}"

    # Set the headers
    headers = {
        "User-Agent": Config.USER_AGENT,
        "Accept": "application/json",
    }

    # Make the request
    return requests.get(url, headers=headers)
