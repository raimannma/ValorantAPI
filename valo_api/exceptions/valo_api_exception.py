from typing import List, Optional, Union

from valo_api.exceptions.rate_limit import RateLimit
from valo_api.responses.error_response import Error, ErrorResponse


class ValoAPIException(Exception):
    """Base exception for all exceptions in the Valo API."""

    ratelimit: RateLimit

    def __init__(self, response: Union[ErrorResponse, str]):
        self.response = response
        self.ratelimit = RateLimit()
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
