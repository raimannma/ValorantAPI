"""

This is a Valorant API Wrapper for https://github.com/Henrik-3/unofficial-valorant-api

"""
import os

from .endpoints import *


def set_api_key(api_key: str):
    """Sets the API key to use for all API requests.

    Args:
        api_key: The API key to use.
    """
    os.environ["VALO_API_KEY"] = api_key
