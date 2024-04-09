from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from model import db, app, Project
from datetime import datetime
date_format = "%Y-%m-%d"

@app.route('/')
def index():
    return render_template("index.html") 

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/detail')
def detail():
    return render_template("detail.html")



@app.route('/project/new', methods = ['GET','POST'])
def projectformm():
    if request.form:
        data = request.form
        print(datetime.date)
        print(data['date'])
        project = Project(title = data['title'], date = datetime.strptime(data['date'],date_format), skills = data['skills'], description = data['desc'], github = data['github'] )
        db.session.add(project)
        db.session.commit()
    return render_template("projectform.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
