from valo_api.utils.dict_struct import DictStruct


class VersionInfoV1(DictStruct):
    version: str
    clientVersion: str
    branch: str
    region: str
