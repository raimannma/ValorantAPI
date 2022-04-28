from typing import Generic, Type, TypeVar

from dataclasses import dataclass

from valo_api.utils.init_options import InitOptions

T = TypeVar("T")


@dataclass
class DataResponse(InitOptions, Generic[T]):
    class_type: Type[T]

    status: int
    data: T

    def __post_init__(self):
        breakpoint()
        self.data = self.class_type.from_dict(**self.data)
