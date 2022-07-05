from typing import Optional, Union

from valo_api.responses.error_response import ErrorResponse


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
        return str(self.response)

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
        return self.response.message

    @property
    def error(self) -> Optional[str]:
        """
        Return the error code of the response.

        Returns:
            The error code of the response.
        """
        if not isinstance(self.response, ErrorResponse):
            return None
        return self.response.error
