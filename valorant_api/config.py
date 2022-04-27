from abc import ABC
from dataclasses import dataclass


@dataclass
class Config(ABC):
    USER_AGENT: str = "Python Valorant API Wrapper"
    BASE_URL: str = "https://api.henrikdev.xyz"
