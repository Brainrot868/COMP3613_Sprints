from flask import Blueprint, url_for

from App.controllers import fastestGraduation

import endpoints
from endpoints import message_types
from endpoints import message
from endpoints import remote

@endpoints.api(name="fastestGrad", version = "v1")
class fastestGradApi(remote.Service)
