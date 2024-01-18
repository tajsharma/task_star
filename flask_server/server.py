import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

#set the base directory to one this file is contained in
basedir = os.path.abspath(os.path.dirname(__file__))
#initiate the app
app =Flask(__name__)

#combine the path to our basedirectory and our database 
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route("/members")
def members():
    return{"members": ["lebron","m2","m3"]}

if __name__ == "__main__":
    app.run(debug=True)