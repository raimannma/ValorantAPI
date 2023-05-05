from typing import (
    Awaitable,
    Callable,
    Dict,
    Generic,
    Iterable,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
)

import io
from dataclasses import dataclass

import msgspec
from PIL import Image
from requests import Response

from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.error_response import ErrorResponse
from valo_api.utils.dict_struct import DictStruct
from valo_api.utils.fetch_endpoint import fetch_endpoint, fetch_endpoint_async

R = TypeVar("R")


def response_type(api_type: R):
    class APIResponse(DictStruct):
        status: int
        data: api_type

    return APIResponse


@dataclass
class Endpoint(Generic[R]):
    path: str
    f_name: str
    return_type: R
    versions: Iterable[str] = ("v1",)
    method: str = "GET"
    kwargs: Optional[Dict[str, Type]] = None
    query_args: Optional[Dict[str, str]] = None
    data_response: bool = True

    def endpoint_wrappers(
        self,
    ) -> Iterable[Tuple[str, Callable[..., Union[R, Awaitable[R]]]]]:
        for version in self.versions:
            yield f"{self.f_name}_{version}", self._get_endpoint_wrapper(version)
            yield f"{self.f_name}_{version}_async", self._get_endpoint_wrapper(
                version, True
            )
        yield self.f_name, self._get_endpoint_wrapper()
        yield f"{self.f_name}_async", self._get_endpoint_wrapper(async_function=True)

    def _get_endpoint_wrapper(
        self, version: Optional[str] = None, async_function: bool = False
    ) -> Union[Callable[..., Union[R, Awaitable[R]]]]:
        if async_function:

            async def wrapper(**kwargs) -> R:
                kwargs["version"] = kwargs.get("version", version)
                for k in self.kwargs.keys():
                    kwargs[k] = kwargs.get(k, "")
                return await self._get_endpoint_async(**kwargs)

        else:

            def wrapper(**kwargs) -> R:
                kwargs["version"] = kwargs.get("version", version)
                for k in self.kwargs.keys():
                    kwargs[k] = kwargs.get(k, "")
                return self._get_endpoint(**kwargs)

        return wrapper

    def build_query_args(self, **kwargs):
        formatted_query_args = (
            {k: v.format(**kwargs) for k, v in self.query_args.items() if v}
            if self.query_args
            else None
        )
        if formatted_query_args is None:
            return {}
        filtered_query_args = {
            k: str(v).lower()
            for k, v in formatted_query_args.items()
            if len(v) > 0 and v.lower() != "none"
        }
        return filtered_query_args

    def _get_endpoint(self, **kwargs) -> R:
        response = fetch_endpoint(
            self.path,
            method=self.method,
            query_args=self.build_query_args(**kwargs),
            **kwargs,
        )
        return self.parse_response(response, response.content)

    async def _get_endpoint_async(self, **kwargs) -> R:
        response, content = await fetch_endpoint_async(
            self.path,
            method=self.method,
            query_args=self.build_query_args(**kwargs),
            **kwargs,
        )
        return self.parse_response(response, content)

    def parse_response(self, response: Response, content: bytes) -> R:
        if response.ok is False:
            error = msgspec.json.decode(content, type=ErrorResponse)
            error.headers = dict(response.headers)
            raise ValoAPIException(error)
        if self.return_type == Image.Image:
            return Image.open(io.BytesIO(response.content))
        return_type = (
            response_type(self.return_type) if self.data_response else self.return_type
        )
        result = msgspec.json.decode(content, type=return_type)
        return result.data if self.data_response else result
