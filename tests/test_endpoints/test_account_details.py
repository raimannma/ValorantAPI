import urllib.parse

import responses
from hypothesis import given
from hypothesis import strategies as st
from responses import matchers

import valo_api
from tests.test_endpoints.utils import get_mock_response
from valo_api.config import Config


@given(
    version=st.sampled_from(["v1"]),
    name=st.text(),
    tag=st.text(),
    force_update=st.booleans(),
)
@responses.activate
def test_get_account_details(version: str, name: str, tag: str, force_update: bool):
    print(f"Test get_account_details with: {locals()}")

    encoded_name = urllib.parse.quote_plus(name).lower()
    encoded_tag = urllib.parse.quote_plus(tag).lower()

    url = f"{Config.BASE_URL}/valorant/{version}/account/{encoded_name}/{encoded_tag}"
    params = {"force": str(force_update).lower()}

    responses.add(
        responses.GET,
        url,
        match=[matchers.query_param_matcher(params)],
        json=get_mock_response(f"account_details_{version}.json"),
        status=200,
    )

    getattr(valo_api, f"get_account_details_{version}")(
        name=name, tag=tag, force_update=force_update
    )
    assert len(responses.calls) == 1

    getattr(valo_api, "get_account_details")(
        version=version, name=name, tag=tag, force_update=force_update
    )
    assert len(responses.calls) == 2


if __name__ == "__main__":
    test_get_account_details()
