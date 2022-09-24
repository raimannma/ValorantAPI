from typing import List

from valo_api.utils.dict_struct import DictStruct


class MatchRaw(DictStruct):
    MatchID: str
    GameStartTime: int
    QueueID: str


class MatchHistoryRawV1(DictStruct):
    Subject: str
    BeginIndex: int
    EndIndex: int
    Total: int
    History: List[MatchRaw]
