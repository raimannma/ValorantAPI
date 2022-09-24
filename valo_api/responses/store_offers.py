from typing import Dict, List

from valo_api.utils.dict_struct import DictStruct


class RewardInfoV1(DictStruct):
    ItemTypeID: str
    ItemID: str
    Quantity: int


class OfferV1(DictStruct):
    OfferID: str
    IsDirectPurchase: bool
    StartDate: str
    Cost: Dict[str, int]
    Rewards: List[RewardInfoV1]


class OfferIDsV1(DictStruct):
    OfferID: str
    StorefrontItemID: str


class StoreOffersV1(DictStruct):
    Offers: List[OfferV1]
    UpgradeCurrencyOffers: List[OfferIDsV1]
