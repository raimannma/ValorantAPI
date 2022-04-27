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
    card: AccountCardV1
    last_update: str

    def __post_init__(self):
        self.card = AccountCardV1.from_dict(**self.card)
