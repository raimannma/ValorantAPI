from typing import Optional

from msgspec import Struct


class WebsiteBannerV1(Struct):
    banner_url: str
    category: str
    date: str
    title: str
    url: str
    external_link: Optional[str] = None
