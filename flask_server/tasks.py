from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.sql import func

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    taskName = db.Column(db.String(100), nullable=False)
    timeStart = db.Column(db.DateTime, default=datetime.utcnow)
    timeSpent = db.Column(db.Integer, default=0)  # Time in minutes
    active = db.Column(db.Boolean, default=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Task {self.taskName}>"
