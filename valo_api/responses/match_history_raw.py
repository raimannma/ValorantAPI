from typing import List

from dataclasses import dataclass

from valo_api.utils.init_options import InitOptions


@dataclass
class MatchRaw(InitOptions):
    MatchID: str
    GameStartTime: int
    QueueID: str


@dataclass
class MatchHistoryRawV1(InitOptions):
    Subject: str
    BeginIndex: int
    EndIndex: int
    Total: int
    History: List[MatchRaw]

    def __post_init__(self):
        self.History = [MatchRaw.from_dict(**m) for m in self.History]
