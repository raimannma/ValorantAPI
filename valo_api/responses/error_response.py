from typing import Dict, List, Optional

from dataclasses import dataclass

from valo_api.utils.init_options import InitOptions


@dataclass
class Error(InitOptions):
    code: Optional[int] = None
    message: Optional[str] = None
    details: Optional[str] = None


@dataclass
class ErrorResponse(InitOptions):
    status: Optional[int] = None
    errors: Optional[List[Error]] = None
    headers: Optional[Dict[str, str]] = None

    def __post_init__(self):
        print(self.errors)
        self.errors = (
            [Error.from_dict(**e) for e in self.errors]
            if self.errors is not None
            else None
        )
