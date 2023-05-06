from typing import List, Optional

from valo_api.utils.dict_struct import DictStruct


class PremierConferencesPodV1(DictStruct):
    pod: str
    name: str


class PremierConferencesV1(DictStruct):
    id: str
    affinity: str
    pods: List[PremierConferencesPodV1]
    region: str
    timezone: str
    name: str
    icon: str
