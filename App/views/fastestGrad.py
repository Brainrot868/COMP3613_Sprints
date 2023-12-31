from flask import Blueprint, url_for

from App.controllers import fastestGraduation

import endpoints
from endpoints import message_types
from endpoints import message
from endpoints import remote

@endpoints.api(name="fastestGrad", version = "v1")
class fastestGradApi(remote.Service)

fastestGrad_views = Blueprint('fastestGrad_views', __name__, template_folder='../templates')

#retrieve route for fastest graduation
@fastestGrad_views.routes('/fastestGrad', methods=['GET'])
def get_fastest_grad_route():
    fastestRoute = fastestGraduation(Student)
    return fastestRoute 
