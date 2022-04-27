from dataclasses import dataclass

from valorant_api.utils.init_options import InitOptions


@dataclass
class ErrorResponse(InitOptions):
    status: int
    message: str
