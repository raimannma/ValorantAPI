from typing import Optional

from valo_api.responses.error_response import ErrorResponse


class ValoAPIException(Exception):
    """
    Base exception for all exceptions in the Valo API.
    """

    def __init__(self, response: ErrorResponse):
        self.response = response
        super().__init__(response)

    def __str__(self):
        return str(self.response)

    @property
    def status(self) -> Optional[int]:
        return self.response.status

    @property
    def message(self) -> Optional[str]:
        return self.response.message

    @property
    def error(self) -> Optional[str]:
        return self.response.error
