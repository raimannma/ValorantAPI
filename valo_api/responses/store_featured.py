from typing import List

from msgspec import Struct


class BundleItemInfoV1(Struct):
    ItemTypeID: str
    ItemID: str
    Amount: int


class BundleItemV1(Struct):
    Item: BundleItemInfoV1
    BasePrice: int
    CurrencyID: str
    DiscountPercent: float
    DiscountedPrice: int
    IsPromoItem: bool


class BundleItemV2(Struct):
    uuid: str
    name: str
    image: str
    type: str
    amount: int
    discount_percent: float
    base_price: int
    discounted_price: int
    promo_item: bool


class BundleV1(Struct):
    ID: str
    DataAssetID: str
    CurrencyID: str
    Items: List[BundleItemV1]
    DurationRemainingInSeconds: int
    WholesaleOnly: bool


class BundleV2(Struct):
    bundle_uuid: str
    items: List[BundleItemV2]
    seconds_remaining: int


class FeaturedBundleV1(Struct):
    Bundle: BundleV1
    Bundles: List[BundleV1]
    BundleRemainingDurationInSeconds: int


class StoreFeaturedV1(Struct):
    FeaturedBundle: FeaturedBundleV1
