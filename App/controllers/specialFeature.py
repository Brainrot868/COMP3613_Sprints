from App.models import CoursePlan, Course
from App.database import db 
from App.controllers import (fastestGraduation, easyCourses, prioritizeElectives)

# Strategy interface
# course plans are made up of 5 courses
class CoursePlanStrategy:
    def execute(self):
        pass

#Implementations
class FastestGraduationStrategy(CoursePlanStrategy):
    def __init__(self, Student):
        self.Student = Student

    def execute(self):
        return fastestGraduation(self.Student)

class EasyCoursesStrategy(CoursePlanStrategy):
    def __init__(self, Student):
        self.Student = Student

    def execute(self):
        return easyCourses(self.Student)

class PrioritizeElectivesStrategy(CoursePlanStrategy):
    def __init__(self, Student):
        self.Student = Student

    def execute(self):
        return fastestGraduation(self.Student)

class CoursePlanContext:
    def __init__(self, strategy: CoursePlanStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: CoursePlanStrategy):
        self.strategy = strategy

    def execute_search(self):
        self.strategy.execute()
