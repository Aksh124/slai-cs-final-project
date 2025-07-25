from os import abort
from flask import app, Flask, render_template, current_app, abort, request
from logic import read_csv

app = Flask(__name__)

data = read_csv("data/data_for_final.csv")

@app.route("/")
def index():
    majors = sorted(set(record["Level and Field of Highest Degree"] for record in data))
    return render_template("index.html",data=data, majors=majors)
    
@app.route("/table")
def show_table():
    return render_template("table_view.html",data=data)
'''
@app.post("")
def submit_form():
    return render_template("", data=data)
'''

@app.post("/")
def college_by_name():
    data2 = [record for record in data if record["Level and Field of Highest Degree"] == request.form["college_major"]]
    if data2:
        return render_template("table_view.html", data=(data2), major_name=request.form["college_major"])
    return render_template("abort.html")

@app.route("/<string:random>")
def random_abort(random):
    return render_template("abort.html")

#@app.route("/college_majors")
#def return_majors():
#read_csv("data/data_for_final.csv"
