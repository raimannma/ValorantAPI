from valo_api.utils.dict_struct import DictStruct


class VersionInfoV1(DictStruct):
    region: str
    branch: str
    build_date: str
    build_ver: str
    last_checked: str
    version: int
    version_for_api: str
