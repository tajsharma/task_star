import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from datetime import datetime

#set the base directory to one this file is contained in
basedir = os.path.abspath(os.path.dirname(__file__))
#initiate the app
app =Flask(__name__)

#combine the path to our basedirectory and our database 
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    taskName = db.Column(db.String(100), nullable=False)
    timeStart = db.Column(db.DateTime, default=datetime.utcnow)
    timeSpent = db.Column(db.Integer, default=0)  # Time in minutes
    active = db.Column(db.Boolean, default=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Task {self.taskName}>"

if __name__ == "__main__":
    app.run(debug=True)



