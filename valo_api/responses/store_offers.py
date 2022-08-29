from typing import Dict, List

from msgspec import Struct


class RewardInfoV1(Struct):
    ItemTypeID: str
    ItemID: str
    Quantity: int


class OfferV1(Struct):
    OfferID: str
    IsDirectPurchase: bool
    StartDate: str
    Cost: Dict[str, int]
    Rewards: List[RewardInfoV1]


class OfferIDsV1(Struct):
    OfferID: str
    StorefrontItemID: str


class StoreOffersV1(Struct):
    Offers: List[OfferV1]
    UpgradeCurrencyOffers: List[OfferIDsV1]
