from msgspec import Struct


class VersionInfoV1(Struct):
    version: str
    clientVersion: str
    branch: str
    region: str
