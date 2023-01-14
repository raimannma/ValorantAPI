from typing import Dict, List, Optional

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


class ContentTierV2(DictStruct):
    name: str
    dev_name: str
    icon: str


class OfferV2(DictStruct):
    offer_id: str
    cost: int
    name: str
    type: str
    icon: Optional[str] = None
    skin_id: Optional[str] = None
    content_tier: Optional[ContentTierV2] = None


class StoreOffersV2(DictStruct):
    offers: List[OfferV2]
