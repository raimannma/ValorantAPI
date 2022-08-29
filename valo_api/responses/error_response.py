from typing import Dict, List, Optional

from msgspec import Struct


class Error(Struct):
    code: Optional[int] = None
    message: Optional[str] = None
    details: Optional[str] = None


class ErrorResponse(Struct):
    status: Optional[int] = None
    errors: Optional[List[Error]] = None
    headers: Optional[Dict[str, str]] = None
