from typing import (
    Awaitable,
    Callable,
    Generic,
    Iterable,
    Optional,
    OrderedDict,
    Tuple,
    Type,
    TypeVar,
    Union,
    get_args,
)

import io
from dataclasses import dataclass

import msgspec
from PIL import Image
from requests import Response

from valo_api.exceptions.valo_api_exception import ValoAPIException
from valo_api.responses.error_response import ErrorResponse
from valo_api.utils.dict_struct import DictStruct
from valo_api.utils.fetch_endpoint import fetch_endpoint

try:
    from valo_api.utils.fetch_endpoint import fetch_endpoint_async
except ImportError:
    pass

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
    kwargs: Optional[OrderedDict[str, Type]] = None
    query_args: Optional[OrderedDict[str, str]] = None
    data_response: bool = True

    def endpoint_wrappers(
        self,
    ) -> Iterable[Tuple[str, Callable[..., Union[R, Awaitable[R]]]]]:
        for version in self.versions:
            yield f"{self.f_name}_{version}", self._get_endpoint_wrapper(version)
            if "fetch_endpoint_async" in globals():
                yield f"{self.f_name}_{version}_async", self._get_endpoint_wrapper(
                    version, True
                )
        yield self.f_name, self._get_endpoint_wrapper()

        if "fetch_endpoint_async" in globals():
            yield f"{self.f_name}_async", self._get_endpoint_wrapper(
                async_function=True
            )

    def _get_endpoint_wrapper(
        self, version: Optional[str] = None, async_function: bool = False
    ) -> Union[Callable[..., Union[R, Awaitable[R]]]]:
        if async_function:

            async def wrapper(*args, **kwargs) -> R:
                kwargs["version"] = kwargs.get("version", version)
                for k in self.kwargs.keys():
                    kwargs[k] = kwargs.get(k, "")
                return await self._get_endpoint_async(*args, **kwargs)

        else:

            def wrapper(*args, **kwargs) -> R:
                kwargs["version"] = kwargs.get("version", version)
                for k in self.kwargs.keys():
                    kwargs[k] = kwargs.get(k, "")
                return self._get_endpoint(*args, **kwargs)

        doc_title = f"{self.f_name} ({version})" if version else self.f_name
        doc_title = doc_title.replace("_", " ").title() + " from the API."
        doc_args = "\n\nArgs:\n"
        if self.kwargs:
            for k, v in self.kwargs.items():
                args = ", ".join(
                    [a.__name__ for a in get_args(v) if a.__name__ != "NoneType"]
                )
                if len(args) > 0:
                    args = f"[{args}]"
                try:
                    doc_args += f"    {k}: {v.__name__}{args}\n"
                except AttributeError:
                    pass
        returns = self.recursive_typing_get_args(self.return_type)
        doc_return = f"\n\nReturns:\n    {returns}: API Fetch Result\n"
        doc_raise = "\n\nRaises:\n    ValoAPIException: If the API returns an error."
        wrapper.__doc__ = doc_title + doc_args + doc_return + doc_raise

        return wrapper

    def recursive_typing_get_args(self, type_: Type) -> str:
        args = get_args(type_)
        if not args or len(args) == 0:
            return f"{type_.__name__}"
        return ", ".join({self.recursive_typing_get_args(arg) for arg in args})

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

    def _get_endpoint(self, *args, **kwargs) -> R:
        args_insert = [a for a in args]
        for k in self.kwargs.keys():
            if k not in kwargs or kwargs[k] is None or kwargs[k] == "":
                kwargs[k] = args_insert.pop(0) if len(args_insert) > 0 else ""
        response = fetch_endpoint(
            self.path,
            method=self.method,
            query_args=self.build_query_args(**kwargs),
            **kwargs,
        )
        return self.parse_response(response, response.content)

    async def _get_endpoint_async(self, *args, **kwargs) -> R:
        args_insert = [a for a in args]
        for k in self.kwargs.keys():
            if k not in kwargs or kwargs[k] is None or kwargs[k] == "":
                kwargs[k] = args_insert.pop(0) if len(args_insert) > 0 else ""
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
