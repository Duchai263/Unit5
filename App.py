from flask import Flask,render_template,request,redirect,flash
from flask_sqlalchemy import SQLAlchemy
from model import db, app, Project
from datetime import datetime
date_format = "%Y-%m-%d"

@app.context_processor
def getProjects():
    projects = Project.query.all()
    for idx,project in enumerate(projects):
        projects[idx].skills = [x.strip() for x in projects[idx].skills.split(',')]
    return dict(projects = projects)

@app.route('/')
def index():
    projects = Project.query.all()
    return render_template("index.html") 

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/project/<id>')
def detail(id):
    id = int(id)
    return render_template("detail.html", id=id-1)

@app.route('/project/<id>/delete')
def detele(id):
    Project.query.filter(Project.id == id).delete()
    db.session.commit()
    return redirect("/")

@app.route('/project/new', methods = ['GET','POST'])
def projectformm():
    if request.method == "POST":
        if request.form:
            data = request.form
            project = Project(title = data['title'], 
                            date = datetime.strptime(data['date'],date_format), 
                            skills = data['skills'], 
                            description = data['desc'], 
                            github = data['github'] )
            db.session.add(project)
            db.session.commit()
            return render_template("projectform.html", message = True)
        else: return redirect("/")

    return render_template("projectform.html", message = False)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
