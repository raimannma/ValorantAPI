from typing import List, Optional, Union

from dataclasses import dataclass

from valo_api.responses.error_response import Error, ErrorResponse
from valo_api.utils.init_options import InitOptions


@dataclass
class RateLimit(InitOptions):
    limit: int
    """The number of requests you did in the current period."""
    remaining: int
    """The number of requests you can make in the current period."""
    reset: int
    """The time in seconds until the current period ends."""


class ValoAPIException(Exception):
    """Base exception for all exceptions in the Valo API."""

    def __init__(self, response: Union[ErrorResponse, str]):
        self.response = response
        super().__init__(response)

    def __str__(self):
        """
        Return the error message.

        Returns:
            The error message as string.
        """
        if not isinstance(self.response, ErrorResponse):
            return self.response

        return f"Errors: {', '.join([e.message for e in self.response.errors])}"

    @property
    def status(self) -> Optional[int]:
        """
        Return the status code of the response.

        Returns:
            The status code of the response.
        """
        if not isinstance(self.response, ErrorResponse):
            return None
        return self.response.status

    @property
    def message(self) -> Optional[str]:
        """
        Return the error message of the response.

        Returns:
            The error message of the response.
        """
        if not isinstance(self.response, ErrorResponse):
            return None
        return ", ".join([e.message for e in self.response.errors])

    @property
    def detail(self) -> Optional[str]:
        """
        Return the error message of the response.

        Returns:
            The error message of the response.
        """
        if not isinstance(self.response, ErrorResponse):
            return None
        return ", ".join([e.details for e in self.response.errors])

    @property
    def errors(self) -> Optional[List[Error]]:
        """
        Return the error code of the response.

        Returns:
            The error code of the response.
        """
        if not isinstance(self.response, ErrorResponse):
            return None
        return self.response.errors

    @property
    def ratelimit(self) -> RateLimit:
        """
        Return the ratelimit of the response.

        Returns:
            RateLimit: The ratelimit of the response.
        """
        return RateLimit.from_dict(
            **{
                "limit": self.response.headers.get("x-ratelimit-limit", None),
                "remaining": self.response.headers.get("x-ratelimit-remaining", None),
                "reset": self.response.headers.get("x-ratelimit-reset", None),
            }
        )
