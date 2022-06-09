from typing import Optional

from dataclasses import dataclass

from valo_api.utils.init_options import InitOptions


@dataclass
class AccountCardV1(InitOptions):
    id: str
    small: str
    large: str
    wide: str


@dataclass
class AccountDetailsV1(InitOptions):
    puuid: str
    region: str
    account_level: int
    name: str
    tag: str
    card: Optional[AccountCardV1] = None
    last_update: Optional[str] = None

    def __post_init__(self):
        self.card = AccountCardV1.from_dict(**self.card) if self.card else None
