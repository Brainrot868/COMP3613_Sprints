from App.database import db
import json

class Grade(db.Model):
    gradeLetter = db.Column(db.String(2), primary_key=True)
    gradeNumber = db.Column(db.Integer)

    # associated_course = db.relationship('Course', back_populates='grade', overlaps="courses")

    def __init__(self, gradeLetter, gradeNumber):
        self.gradeLetter = gradeLetter
        self.gradeNumber = gradeNumber

    def get_json(self):
        return {
            'Grade Letter' : self.gradeLetter,
            'Grade Number' : self.gradeNumber,
        }