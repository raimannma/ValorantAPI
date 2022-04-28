from typing import Dict, List

from dataclasses import dataclass

from valo_api.utils.init_options import InitOptions


@dataclass
class RewardInfoV1(InitOptions):
    ItemTypeID: str
    ItemID: str
    Quantity: int


@dataclass
class OfferV1(InitOptions):
    OfferID: str
    IsDirectPurchase: bool
    StartDate: str
    Cost: Dict[str, int]
    Rewards: List[RewardInfoV1]

    def __post_init__(self):
        self.Rewards = [RewardInfoV1.from_dict(**r) for r in self.Rewards]


@dataclass
class OfferIDsV1(InitOptions):
    OfferID: str
    StorefrontItemID: str


@dataclass
class StoreOffersV1(InitOptions):
    Offers: List[OfferV1]
    UpgradeCurrencyOffers: List[OfferIDsV1]

    def __post_init__(self):
        self.Offers = [OfferV1.from_dict(**o) for o in self.Offers]
        self.UpgradeCurrencyOffers = [
            OfferIDsV1.from_dict(**o) for o in self.UpgradeCurrencyOffers
        ]
