from flask import Blueprint, url_for
from App.models import Program, ProgramCourses

from App.controllers import easyCourses

import endpoints
from endpoints import message_types
from endpoints import message
from endpoints import remote

@endpoints.api(name="easiestCourses", version = "v1")
class easiestCoursesApi(remote.Service)
