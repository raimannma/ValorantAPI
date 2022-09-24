from typing import Optional

from valo_api.utils.dict_struct import DictStruct


class WebsiteBannerV1(DictStruct):
    banner_url: str
    category: str
    date: str
    title: str
    url: str
    external_link: Optional[str] = None
