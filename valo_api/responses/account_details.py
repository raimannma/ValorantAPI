from typing import Optional

from msgspec import Struct


class AccountCardV1(Struct):
    id: str
    small: str
    large: str
    wide: str


class AccountDetailsV1(Struct):
    puuid: str
    region: str
    account_level: int
    name: str
    tag: str
    card: Optional[AccountCardV1] = None
    last_update: Optional[str] = None
    last_update_raw: Optional[int] = None
