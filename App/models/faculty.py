from App.database import db
import json

class Faculty(db.Model):
    facultyID = db.Column(db.Integer, primary_key=True)
    facultyName = db.Column(db.String(50))

    def __init__(self, id, facName):
        self.facultyID = id
        self.facName = facName

    def get_json(self):
        return {
            'Faulty ID' : self.facultyID,
            'Faculty Name' : self.facName,
        }