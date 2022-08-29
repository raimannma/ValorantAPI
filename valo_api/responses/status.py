from typing import List, Optional

from msgspec import Struct


class MaintenanceStatusTitleV1(Struct):
    locale: str
    content: str


class MaintenanceUpdateV1(Struct):
    publish_locations: List[str]
    updated_at: str
    created_at: str
    id: int
    publish: bool
    translations: List[MaintenanceStatusTitleV1]
    author: Optional[str] = None


class MaintenancePointV1(Struct):
    updated_at: Optional[str]
    created_at: Optional[str]
    archive_at: Optional[str]
    titles: List[MaintenanceStatusTitleV1]
    maintenance_status: str
    id: int
    incident_severity: Optional[str]
    updates: List[MaintenanceUpdateV1]
    platforms: List[str]


class StatusV1(Struct):
    maintenances: List[MaintenancePointV1]
    incidents: List[MaintenancePointV1]
