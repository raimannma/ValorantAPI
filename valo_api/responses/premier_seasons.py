from typing import List, Optional

from valo_api.utils.dict_struct import DictStruct


class PremierSeasonEventConferenceScheduleV1(DictStruct):
    conference: str
    starts_at: str
    ends_at: str


class PremierSeasonEventMapSelectionMapV1(DictStruct):
    name: str
    id: str


class PremierSeasonEventMapSelectionV1(DictStruct):
    type: str
    maps: Optional[List[PremierSeasonEventMapSelectionMapV1]]


class PremierSeasonEventV1(DictStruct):
    id: str
    type: str
    starts_at: str
    ends_at: str
    conference_schedules: Optional[List[PremierSeasonEventConferenceScheduleV1]]
    map_selection: PremierSeasonEventMapSelectionV1
    points_required_to_participate: int


class PremierSeasonV1(DictStruct):
    id: str
    championship_event_id: str
    championship_points_required: int
    starts_at: str
    ends_at: str
    enrollment_starts_at: str
    enrollment_ends_at: str
    events: List[PremierSeasonEventV1]
