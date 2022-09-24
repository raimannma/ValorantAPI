from typing import List

from valo_api.utils.dict_struct import DictStruct


class BundleItemInfoV1(DictStruct):
    ItemTypeID: str
    ItemID: str
    Amount: int


class BundleItemV1(DictStruct):
    Item: BundleItemInfoV1
    BasePrice: int
    CurrencyID: str
    DiscountPercent: float
    DiscountedPrice: int
    IsPromoItem: bool


class BundleItemV2(DictStruct):
    uuid: str
    name: str
    image: str
    type: str
    amount: int
    discount_percent: float
    base_price: int
    discounted_price: int
    promo_item: bool


class BundleV1(DictStruct):
    ID: str
    DataAssetID: str
    CurrencyID: str
    Items: List[BundleItemV1]
    DurationRemainingInSeconds: int
    WholesaleOnly: bool


class BundleV2(DictStruct):
    bundle_uuid: str
    bundle_price: int
    items: List[BundleItemV2]
    seconds_remaining: int
    whole_sale_only: bool


class FeaturedBundleV1(DictStruct):
    Bundle: BundleV1
    Bundles: List[BundleV1]
    BundleRemainingDurationInSeconds: int


class StoreFeaturedV1(DictStruct):
    FeaturedBundle: FeaturedBundleV1
