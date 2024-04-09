from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date, ARRAY, Text
from datetime import datetime

app = Flask(__name__,static_folder="static")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///projects.db"
db = SQLAlchemy(app)

class Project(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String)
    date = Column(Date,default=datetime.now().date())
    description = Column(Text)
    skills = Column(String)
    github = Column(String)

    def __repr__(self):
        return f"""Project: (Title: {self.title}
                            Date: {self.date}
                            Description: {self.description}
                            Skills: {self.skills}
                            Github: {self.github})"""
