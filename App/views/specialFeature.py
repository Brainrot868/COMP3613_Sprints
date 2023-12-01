from flask import Blueprint, url_for

from App.controllers import specialFeature

import endpoints
from endpoints import message_types
from endpoints import message
from endpoints import remote

@endpoints.api(name="speacialFeature", version = "v1")
class easiestCoursesApi(remote.Service)

speacialFeature_views = Blueprint('speacialFeature_views', __name__, tamplates_folder='../templates')

@speacialFeature_views.route('/specialFeature', methods=['GET'])
def specialFeatureFunction():
    coursePlan = CoursePlanStrategy()
    return coursePlan
