from typing import List

from dataclasses import dataclass

from valo_api.utils.init_options import InitOptions


@dataclass
class BundleItemInfoV1(InitOptions):
    ItemTypeID: str
    ItemID: str
    Amount: int


@dataclass
class BundleItemV1(InitOptions):
    Item: BundleItemInfoV1
    BasePrice: int
    CurrencyID: str
    DiscountPercent: float
    DiscountedPrice: int
    IsPromoItem: bool

    def __post_init__(self):
        self.Item = BundleItemInfoV1.from_dict(**self.Item)


@dataclass
class BundleItemV2(InitOptions):
    uuid: str
    name: str
    image: str
    type: str
    amount: int
    discount_percent: float
    base_price: int
    discounted_price: int
    promo_item: bool


@dataclass
class BundleV1(InitOptions):
    ID: str
    DataAssetID: str
    CurrencyID: str
    Items: List[BundleItemV1]
    DurationRemainingInSeconds: int
    WholesaleOnly: bool

    def __post_init__(self):
        self.Items = [BundleItemV1.from_dict(**item) for item in self.Items]


@dataclass
class BundleV2(InitOptions):
    bundle_uuid: str
    items: List[BundleItemV2]
    seconds_remaining: int

    def __post_init__(self):
        self.items = [BundleItemV2.from_dict(**item) for item in self.items]


@dataclass
class FeaturedBundleV1(InitOptions):
    Bundle: BundleV1
    Bundles: List[BundleV1]
    BundleRemainingDurationInSeconds: int

    def __post_init__(self):
        self.Bundle = BundleV1.from_dict(**self.Bundle)
        self.Bundles = [BundleV1.from_dict(**bundle) for bundle in self.Bundles]


@dataclass
class StoreFeaturedV1(InitOptions):
    FeaturedBundle: FeaturedBundleV1

    def __post_init__(self):
        self.FeaturedBundle = FeaturedBundleV1.from_dict(**self.FeaturedBundle)
