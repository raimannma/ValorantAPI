from typing import List, Optional

from valo_api.utils.dict_struct import DictStruct


class MaintenanceStatusTitleV1(DictStruct):
    locale: str
    content: str


class MaintenanceUpdateV1(DictStruct):
    publish_locations: List[str]
    updated_at: str
    created_at: str
    id: int
    publish: bool
    translations: List[MaintenanceStatusTitleV1]
    author: Optional[str] = None


class MaintenancePointV1(DictStruct):
    updated_at: Optional[str]
    created_at: Optional[str]
    archive_at: Optional[str]
    titles: List[MaintenanceStatusTitleV1]
    maintenance_status: str
    id: int
    incident_severity: Optional[str]
    updates: List[MaintenanceUpdateV1]
    platforms: List[str]


class StatusV1(DictStruct):
    maintenances: List[MaintenancePointV1]
    incidents: List[MaintenancePointV1]
