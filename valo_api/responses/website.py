from dataclasses import dataclass

from valo_api.utils.init_options import InitOptions


@dataclass
class WebsiteBannerV1(InitOptions):
    banner_url: str
    category: str
    date: str
    external_link: str
    title: str
    url: str
