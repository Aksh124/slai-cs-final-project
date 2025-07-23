import csv
from flask import current_app

def read_csv(filename: str):
    result = []
    with open(filename, "r") as file:
        for record in csv.DictReader(file):
            result.append(record)
    return result

def query(form: dict):
    result = []
    element = read_csv("data_for_final.csv")
    for element in current_app.data:
        if form["college_major"] != element["Level and Field of Highest Degree"]: 
            continue
        result.append(element)
    return result