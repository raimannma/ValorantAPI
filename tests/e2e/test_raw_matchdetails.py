from time import sleep

from hypothesis import given, settings
from hypothesis import strategies as st

import valo_api
from valo_api.endpoints.raw import EndpointType
from valo_api.exceptions.rate_limit import rate_limit


@settings(deadline=None, max_examples=15)
@given(
    version=st.sampled_from(["v1"]),
    puuid=st.sampled_from(
        [
            "84d16a5c-5e72-434f-884a-23d6a9283307",
            "6132647f-9e1a-45d5-bdfe-a5e7044c3d24",
            "f06d533f-1698-47bb-830e-27991afce46f",
            "a081c970-9406-4cdc-83fa-29e382e67d4a",
            "49d0c412-1393-4dc0-8175-8f1c29785055",
        ]
    ),
)
def test_get_raw_matchdetails(version: str, puuid: str):
    sleep(rate_limit().reset + 1 if rate_limit().remaining <= 2 else 0)
    print(f"Test get_raw_matchdetails with: {locals()}")

    getattr(valo_api, f"get_raw_data_{version}")(
        type=EndpointType.MATCH_DETAILS, region="eu", value=puuid
    )


if __name__ == "__main__":
    test_get_raw_matchdetails()
