from valo_api.endpoint import Endpoint
from valo_api.endpoints_config import EndpointsConfig

function_names = []
for name, value in EndpointsConfig.__dict__.items():
    if hasattr(value, "value") and isinstance(value.value, Endpoint):
        for name, function in value.value.endpoint_wrappers():
            function_names.append(name)
            globals()[name] = function

__all__ = function_names
