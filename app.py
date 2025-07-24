from os import abort
from flask import app, Flask, render_template, current_app, abort
from logic import read_csv

app = Flask(__name__)

data = read_csv("data/data_for_final.csv")

@app.route("/")
def index():
    return render_template("index.html",data=data)
    
@app.route("/table")
def show_table():
    return render_template("table_view.html",data=data)
'''
@app.post("")
def submit_form():
    return render_template("", data=data)
'''

@app.post("/<string:major_name>")
def college_by_name(major_name: str):
    data2 = [record for record in data if record["Level and Field of Highest Degree"] == major_name]
    if data2:
        return render_template("table_view.html", data=data2)
    abort(404)

#@app.route("/college_majors")
#def return_majors():
#read_csv("data/data_for_final.csv"
