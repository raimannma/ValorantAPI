from typing import List


class Config:
    USER_AGENT: str = "Python Valorant API Wrapper"
    BASE_URL: str = "https://api.henrikdev.xyz"
    ALL_REGIONS: List[str] = ["eu", "na", "ap", "kr", "latam", "br"]
    ALL_COUNTRY_CODES = [
        "en-us",
        "en-gb",
        "de-de",
        "es-es",
        "fr-fr",
        "it-it",
        "ru-ru",
        "tr-tr",
        "es-mx",
        "ja-jp",
        "ko-kr",
        "pt-br",
        "vi-vn",
    ]
    ALL_LOCALS = [
        "ar-AE",
        "de-DE",
        "en-US",
        "es-ES",
        "es-MX",
        "fr-FR",
        "id-ID",
        "it-IT",
        "ja-JP",
        "ko-KR",
        "pl-PL",
        "pt-BR",
        "ru-RU",
        "th-TH",
        "tr-TR",
        "vi-VN",
        "zh-CN",
        "zh-TW",
    ]
