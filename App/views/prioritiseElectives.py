from flask import Blueprint, url_for
from App.models import Program, ProgramCourses

from App.controllers import prioritzeElectives

import endpoints
from endpoints import message_types
from endpoints import message
from endpoints import remote

@endpoints.api(name="priotiseElectives", version = "v1")
class priotiseElectivesApi(remote.Service)

prioritiseElectives_views = Blueprint('prioritiseElectives_views', __name__, template_folder='../templates')

@prioritiseElectives_views.route('/prioritiseElectives', methods=['GET'])
def get_priority_electives():
    priorityElectives = prioritizeElectives(Student)
    return priorityElectives


