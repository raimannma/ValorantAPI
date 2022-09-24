from typing import Optional

from valo_api.utils.dict_struct import DictStruct


class AccountCardV1(DictStruct):
    id: str
    small: str
    large: str
    wide: str


class AccountDetailsV1(DictStruct):
    puuid: str
    region: str
    account_level: int
    name: str
    tag: str
    card: Optional[AccountCardV1] = None
    last_update: Optional[str] = None
    last_update_raw: Optional[int] = None
