from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def about():
    return render_template("index.html") 

@app.route('/projectform')
def pronjectfrom():
    return render_template("detail.html")       