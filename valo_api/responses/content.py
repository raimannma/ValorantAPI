from typing import Dict, List, Optional

from msgspec import Struct


class Entity(Struct):
    name: str
    id: str
    assetName: str
    assetPath: Optional[str] = None
    localizedNames: Optional[Dict[str, str]] = None


class Act(Struct):
    id: str
    parentId: str
    type: str
    name: str
    isActive: bool
    localizedNames: Optional[Dict[str, str]] = None


class ContentV1(Struct):
    version: str
    characters: List[Entity]
    maps: List[Entity]
    chromas: List[Entity]
    skins: List[Entity]
    skinLevels: List[Entity]
    equips: List[Entity]
    gameModes: List[Entity]
    sprays: List[Entity]
    sprayLevels: List[Entity]
    charms: List[Entity]
    charmLevels: List[Entity]
    playerCards: List[Entity]
    playerTitles: List[Entity]
    acts: List[Act]
    ceremonies: List[Entity]
