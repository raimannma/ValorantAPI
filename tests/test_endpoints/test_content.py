import responses
from hypothesis import given, settings
from hypothesis import strategies as st
from responses import matchers

import valo_api
from tests.test_endpoints.utils import get_mock_response
from valo_api.config import Config


@settings(deadline=None)
@given(version=st.sampled_from(["v1"]), locale=st.sampled_from(Config.ALL_LOCALS))
@responses.activate
def test_get_content(version: str, locale: str):
    print(f"Test get_content with: {locals()}")

    locale = str(locale).lower()

    url = f"{Config.BASE_URL}/valorant/{version}/content"
    params = {"locale": locale}

    responses.add(
        responses.GET,
        url,
        match=[matchers.query_param_matcher(params)],
        json=get_mock_response(f"content_{version}.json"),
        status=200,
    )

    getattr(valo_api, f"get_content_{version}")(locale=locale)
    assert len(responses.calls) == 1

    getattr(valo_api, "get_content")(version=version, locale=locale)
    assert len(responses.calls) == 2


if __name__ == "__main__":
    test_get_content()
