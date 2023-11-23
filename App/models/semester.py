from App.database import db
import json

class Semester(db.Model):
    semesterID = db.Column(db.String(1), primary_key=True)

    def __init__(self, id):
        this.semesterID = id

    def get_json(self):
        return { 'Semester ID' : self.semesterID }