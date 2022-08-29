from typing import List

from msgspec import Struct


class MatchRaw(Struct):
    MatchID: str
    GameStartTime: int
    QueueID: str


class MatchHistoryRawV1(Struct):
    Subject: str
    BeginIndex: int
    EndIndex: int
    Total: int
    History: List[MatchRaw]
