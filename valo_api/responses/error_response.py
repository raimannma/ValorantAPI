from typing import Dict, List, Optional

from valo_api.utils.dict_struct import DictStruct


class Error(DictStruct):
    code: Optional[int] = None
    message: Optional[str] = None
    details: Optional[str] = None


class ErrorResponse(DictStruct):
    status: Optional[int] = None
    errors: Optional[List[Error]] = None
    headers: Optional[Dict[str, str]] = None
