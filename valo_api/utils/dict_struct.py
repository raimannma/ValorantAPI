from msgspec import Struct


class DictStruct(Struct):
    def to_dict(self):
        return {f: getattr(self, f) for f in self.__struct_fields__}

    @property
    def __dict__(self):
        return self.to_dict()
