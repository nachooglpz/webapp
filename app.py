import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:test@127.0.0.1:3306/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(100), nullable = False)
    last_name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(80), unique = True, nullable = False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone = True), server_default = func.now())
    bio = db.Column(db.Text)

def __repr__(self):
        return f'<Student {self.first_name}>'

@app.route("/")
def hello_world():
    return "<p>Hello, world!</p>"

@app.route("/usuario/<name>")
def hello_usuario(name):
    return f"<p>Hello, {name}!</p>"

@app.route("/estudiantes")
def estudiantes():
     students = Student.query.all()
     #return students[0].first_name + " " + students[1].first_name + " " + students[2].first_name + " " + students[3].first_name + " " + students[4].first_name
     return render_template("estudiantes.html", students = students)