from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from model import db, app, Project

@app.route('/')
def index():
    return render_template("index.html") 

@app.route('/about')
def about():
    return render_template("about.html")



@app.route('/project/new', methods = ['GET','POST'])
def pronjectfrom():
    if request.form:
        print(request.form)
    return render_template("projectform.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
