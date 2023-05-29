import json
import urllib

import valo_api

if __name__ == "__main__":
    obj = {"startIndex": 0, "endIndex": 20}
    query = f"?{urllib.parse.urlencode(obj)}"
    print(
        valo_api.endpoints.get_raw_competitive_updates_data_v1(
            "ee89b4d9-13d0-5832-8dd7-eb5d8806d918",
            "eu",
            {"startIndex": 0, "endIndex": 20},
        )
    )
