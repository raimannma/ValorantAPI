import pytest
import responses
from aioresponses import aioresponses
from hypothesis import given
from hypothesis import strategies as st
from responses import matchers

import valo_api
from tests.unit.endpoints.utils import get_error_responses, validate_exception
from valo_api.config import Config
from valo_api.exceptions.valo_api_exception import ValoAPIException


@given(
    version=st.sampled_from(["v1"]),
    crosshair_id=st.sampled_from(["0;P;h;0;f;0;0l;4;0o;0;0a;1;0f;0;1b;0"]),
    error_response=st.sampled_from(get_error_responses("crosshair")),
)
@responses.activate
@pytest.mark.asyncio
async def test_get_crosshair_error(
    version: str, crosshair_id: str, error_response: dict
):
    print(f"Test get_crosshair with: {locals()}")

    url = f"{Config.BASE_URL}/valorant/{version}/crosshair/generate"

    crosshair_id = crosshair_id.lower()
    params = {"id": crosshair_id}

    responses.add(
        responses.GET,
        url,
        match=[matchers.query_param_matcher(params)],
        json=error_response,
        status=int(error_response["status"]) if "status" in error_response else 500,
    )

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, f"get_crosshair_{version}")(crosshair_id=crosshair_id)
        validate_exception(error_response, excinfo)
    assert len(responses.calls) == 1

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, "get_crosshair")(version=version, crosshair_id=crosshair_id)
        validate_exception(error_response, excinfo)
    assert len(responses.calls) == 2

    with aioresponses() as m:
        m.get(
            f"{url}?id={crosshair_id}",
            payload=error_response,
            exception=ValoAPIException(error_response),
        )
        with pytest.raises(ValoAPIException) as excinfo:
            await getattr(valo_api, f"get_crosshair_{version}_async")(
                crosshair_id=crosshair_id
            )
            validate_exception(error_response, excinfo)
        m.assert_called_once()

    with aioresponses() as m:
        m.get(
            f"{url}?id={crosshair_id}",
            payload=error_response,
            exception=ValoAPIException(error_response),
        )
        with pytest.raises(ValoAPIException) as excinfo:
            await getattr(valo_api, "get_crosshair_async")(
                version=version, crosshair_id=crosshair_id
            )
            validate_exception(error_response, excinfo)
        m.assert_called_once()


if __name__ == "__main__":
    test_get_crosshair_error()
