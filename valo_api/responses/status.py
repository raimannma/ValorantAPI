from typing import List, Optional

from dataclasses import dataclass

from valo_api.utils.init_options import InitOptions


@dataclass
class MaintenanceStatusTitleV1(InitOptions):
    locale: str
    content: str


@dataclass
class MaintenanceUpdateV1(InitOptions):
    publish_locations: List[str]
    updated_at: str
    created_at: str
    id: int
    publish: bool
    translations: List[MaintenanceStatusTitleV1]
    author: Optional[str] = None

    def __post_init__(self):
        self.translations = [MaintenanceStatusTitleV1(**t) for t in self.translations]


@dataclass
class MaintenancePointV1(InitOptions):
    updated_at: Optional[str]
    created_at: Optional[str]
    archive_at: Optional[str]
    titles: List[MaintenanceStatusTitleV1]
    maintenance_status: str
    id: int
    incident_severity: Optional[str]
    updates: List[MaintenanceUpdateV1]
    platforms: List[str]

    def __post_init__(self):
        self.titles = [MaintenanceStatusTitleV1.from_dict(**t) for t in self.titles]
        self.updates = [MaintenanceUpdateV1.from_dict(**u) for u in self.updates]


@dataclass
class StatusV1(InitOptions):
    maintenances: List[MaintenancePointV1]
    incidents: List[MaintenancePointV1]

    def __post_init__(self):
        self.maintenances = [
            MaintenancePointV1.from_dict(**m) for m in self.maintenances
        ]
        self.incidents = [MaintenancePointV1.from_dict(**i) for i in self.incidents]
