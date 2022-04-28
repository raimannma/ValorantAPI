from typing import Optional

import urllib.parse
from uuid import UUID

import responses
from hypothesis import given, settings
from hypothesis import strategies as st
from responses import matchers

import valo_api
from tests.test_endpoints.utils import get_mock_response
from valo_api.config import Config


@given(
    version=st.sampled_from(["v1", "v2"]),
    region=st.sampled_from(Config.ALL_REGIONS),
    name=st.text(),
    tag=st.text(),
    filter=st.one_of(st.none(), st.text(min_size=5, max_size=5)),
)
@responses.activate
def test_get_mmr_details_by_name(
    version: str, region: str, name: str, tag: str, filter: Optional[str]
):
    print(f"Test get_mmr_details_by_name with: {locals()}")

    filter = str(filter).lower() if filter is not None and version == "v2" else None
    encoded_name = urllib.parse.quote_plus(name).lower()
    encoded_tag = urllib.parse.quote_plus(tag).lower()

    url = f"{Config.BASE_URL}/valorant/{version}/mmr/{region}/{encoded_name}/{encoded_tag}"
    params = {"filter": filter} if filter is not None and version == "v2" else {}

    responses.add(
        responses.GET,
        url,
        json=get_mock_response(f"mmr_details_by_name_{version}.json"),
        match={matchers.query_param_matcher(params)},
        status=200,
    )

    getattr(valo_api, f"get_mmr_details_by_name_{version}")(
        region=region, name=name, tag=tag, filter=filter
    )
    assert len(responses.calls) == 1

    getattr(valo_api, "get_mmr_details_by_name")(
        version=version, region=region, name=name, tag=tag, filter=filter
    )
    assert len(responses.calls) == 2


@given(
    version=st.sampled_from(["v1", "v2"]),
    region=st.sampled_from(Config.ALL_REGIONS),
    puuid=st.uuids(),
    filter=st.one_of(st.none(), st.text(min_size=5, max_size=5)),
)
@responses.activate
def test_get_mmr_details_by_puuid(
    version: str, region: str, puuid: UUID, filter: Optional[str]
):
    print(f"Test get_mmr_details_by_puuid with: {locals()}")

    puuid = str(puuid).lower()
    filter = str(filter).lower() if filter is not None and version == "v2" else None

    url = f"{Config.BASE_URL}/valorant/{version}/by-puuid/mmr/{region}/{puuid}"
    params = {"filter": filter} if filter is not None and version == "v2" else {}

    responses.add(
        responses.GET,
        url,
        json=get_mock_response(f"mmr_details_by_puuid_{version}.json"),
        match={matchers.query_param_matcher(params)},
        status=200,
    )

    getattr(valo_api, f"get_mmr_details_by_puuid_{version}")(
        region=region, puuid=puuid, filter=filter
    )
    assert len(responses.calls) == 1

    getattr(valo_api, "get_mmr_details_by_puuid")(
        version=version, region=region, puuid=puuid, filter=filter
    )
    assert len(responses.calls) == 2


if __name__ == "__main__":
    test_get_mmr_details_by_name()
    test_get_mmr_details_by_puuid()
