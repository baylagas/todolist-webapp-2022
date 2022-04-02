from utils.db import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80), nullable=False)
    isFinished = db.Column(db.Boolean, nullable=False)

    def __init__(self, description, isFinished=False) -> None:
        self.description = description
        self.isFinished = isFinished

    def __repr__(self) -> str:
        return f"Task({self.id}, '{self.description}', {self.isFinished})"
