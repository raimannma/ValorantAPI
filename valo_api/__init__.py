"""

This is a Valorant API Wrapper for https://github.com/Henrik-3/unofficial-valorant-api

"""
import os

from .endpoints import *
from .exceptions.rate_limit import RateLimit


def set_api_key(api_key: str):
    """Sets the API key to use for all API requests.

    Args:
        api_key: The API key to use.
    """
    os.environ["VALO_API_KEY"] = api_key


def rate_limit() -> RateLimit:
    """Returns the current rate limit for the API.

    Returns:
        RateLimit: A :class:`.RateLimit` object.
    """
    return RateLimit()
