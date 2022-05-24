from dataclasses import dataclass

from valo_api.utils.init_options import InitOptions


@dataclass
class VersionInfoV1(InitOptions):
    version: str
    clientVersion: str
    branch: str
    region: str
