# type: ignore[attr-defined]
"""Valorant API Wrapper for https://github.com/Henrik-3/unofficial-valorant-api"""

import sys
from importlib import metadata as importlib_metadata


def get_version() -> str:
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return "unknown"


version: str = get_version()
