from typing import Dict, List, Optional

from dataclasses import dataclass

from valo_api.utils.init_options import InitOptions


@dataclass
class Entity(InitOptions):
    name: str
    id: str
    assetName: str
    assetPath: Optional[str] = None
    localizedNames: Optional[Dict[str, str]] = None


@dataclass
class Act(InitOptions):
    id: str
    parentId: str
    type: str
    name: str
    isActive: bool
    localizedNames: Optional[Dict[str, str]] = None


@dataclass
class ContentV1(InitOptions):
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

    def __post_init__(self):
        self.characters = [Entity.from_dict(**c) for c in self.characters]
        self.maps = [Entity.from_dict(**m) for m in self.maps]
        self.chromas = [Entity.from_dict(**c) for c in self.chromas]
        self.skins = [Entity.from_dict(**s) for s in self.skins]
        self.skinLevels = [Entity.from_dict(**sl) for sl in self.skinLevels]
        self.equips = [Entity.from_dict(**e) for e in self.equips]
        self.gameModes = [Entity.from_dict(**gm) for gm in self.gameModes]
        self.sprays = [Entity.from_dict(**s) for s in self.sprays]
        self.sprayLevels = [Entity.from_dict(**sl) for sl in self.sprayLevels]
        self.charms = [Entity.from_dict(**c) for c in self.charms]
        self.charmLevels = [Entity.from_dict(**cl) for cl in self.charmLevels]
        self.playerCards = [Entity.from_dict(**pc) for pc in self.playerCards]
        self.playerTitles = [Entity.from_dict(**pt) for pt in self.playerTitles]
        self.acts = [Act.from_dict(**a) for a in self.acts]
        self.ceremonies = [Entity.from_dict(**c) for c in self.ceremonies]
