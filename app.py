from flask import app, Flask, render_template
from logic import read_csv

app = Flask(__name__)

data = read_csv("data/data_for_final.csv")

@app.route("/")
def index():
    return render_template("base.html",data=data)
    
@app.route("/table")
def index_new():
    return render_template("table_view.html",data=data)
    

#@app.route("/college_majors")
#def return_majors():
    