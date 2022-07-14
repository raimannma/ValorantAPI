from typing import Dict, Optional

from dataclasses import dataclass

from valo_api.utils.init_options import InitOptions


@dataclass
class ErrorResponse(InitOptions):
    status: Optional[int] = None
    message: Optional[str] = None
    error: Optional[str] = None
    headers: Optional[Dict[str, str]] = None
