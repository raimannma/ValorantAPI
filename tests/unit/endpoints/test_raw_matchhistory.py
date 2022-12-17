from uuid import UUID

import pytest
import responses
from aioresponses import aioresponses
from hypothesis import given
from hypothesis import strategies as st

import valo_api
from tests.unit.endpoints.utils import get_mock_response
from valo_api.config import Config
from valo_api.endpoints.raw import EndpointType


@given(
    version=st.sampled_from(["v1"]),
    match_id=st.uuids(),
    region=st.sampled_from(Config.ALL_REGIONS),
)
@responses.activate
@pytest.mark.asyncio
async def test_get_raw_matchhistory(version: str, match_id: UUID, region: str):
    print(f"Test get_raw_matchhistory with: {locals()}")

    url = f"{Config.BASE_URL}/valorant/{version}/raw"

    match_id = str(match_id).lower()

    responses.add(
        responses.POST,
        url,
        json=get_mock_response(f"raw_matchhistory_{version}.json"),
        status=200,
    )

    getattr(valo_api, f"get_raw_data_{version}")(
        type=EndpointType.MATCH_HISTORY, region=region, value=match_id
    )
    assert len(responses.calls) == 1

    getattr(valo_api, "get_raw_data")(
        version=version,
        type=EndpointType.MATCH_HISTORY,
        region=region,
        value=match_id,
    )
    assert len(responses.calls) == 2

    with aioresponses() as m:
        m.post(
            f"{url}?region={region}&type=matchhistory&value={match_id}",
            payload=get_mock_response(f"raw_matchhistory_{version}.json"),
        )
        await getattr(valo_api, f"get_raw_data_{version}_async")(
            type=EndpointType.MATCH_HISTORY, region=region, value=match_id
        )
        m.assert_called_once()

    with aioresponses() as m:
        m.post(
            f"{url}?region={region}&type=matchhistory&value={match_id}",
            payload=get_mock_response(f"raw_matchhistory_{version}.json"),
        )
        await getattr(valo_api, "get_raw_data_async")(
            version=version,
            type=EndpointType.MATCH_HISTORY,
            region=region,
            value=match_id,
        )
        m.assert_called_once()


if __name__ == "__main__":
    test_get_raw_matchhistory()
