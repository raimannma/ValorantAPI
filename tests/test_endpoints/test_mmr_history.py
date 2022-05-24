import urllib.parse
from uuid import UUID

import responses
from hypothesis import given
from hypothesis import strategies as st

import valo_api
from tests.test_endpoints.utils import get_mock_response
from valo_api.config import Config


@given(
    version=st.sampled_from(["v1"]),
    region=st.sampled_from(Config.ALL_REGIONS),
    name=st.text(),
    tag=st.text(),
)
@responses.activate
def test_get_mmr_history_by_name(version: str, region: str, name: str, tag: str):
    print(f"Test get_mmr_history_by_name with: {locals()}")

    encoded_name = urllib.parse.quote_plus(name).lower()
    encoded_tag = urllib.parse.quote_plus(tag).lower()

    url = f"{Config.BASE_URL}/valorant/{version}/mmr-history/{region}/{encoded_name}/{encoded_tag}"

    responses.add(
        responses.GET,
        url,
        json=get_mock_response(f"mmr_history_by_name_{version}.json"),
        status=200,
    )

    getattr(valo_api, f"get_mmr_history_by_name_{version}")(
        region=region, name=name, tag=tag
    )
    assert len(responses.calls) == 1

    getattr(valo_api, "get_mmr_history_by_name")(
        version=version, region=region, name=name, tag=tag
    )
    assert len(responses.calls) == 2


@given(
    version=st.sampled_from(["v1"]),
    region=st.sampled_from(Config.ALL_REGIONS),
    puuid=st.uuids(),
)
@responses.activate
def test_get_mmr_history_by_puuid(version: str, region: str, puuid: UUID):
    print(f"Test get_mmr_history_by_puuid with: {locals()}")

    puuid = str(puuid).lower()

    url = f"{Config.BASE_URL}/valorant/{version}/by-puuid/mmr-history/{region}/{puuid}"

    responses.add(
        responses.GET,
        url,
        json=get_mock_response(f"mmr_history_by_puuid_{version}.json"),
        status=200,
    )

    getattr(valo_api, f"get_mmr_history_by_puuid_{version}")(region=region, puuid=puuid)
    assert len(responses.calls) == 1

    getattr(valo_api, "get_mmr_history_by_puuid")(
        version=version, region=region, puuid=puuid
    )
    assert len(responses.calls) == 2


if __name__ == "__main__":
    test_get_mmr_history_by_name()
    test_get_mmr_history_by_puuid()
