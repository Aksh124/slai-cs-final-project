import csv

def read_csv(filename: str):
    result = []
    with open(filename, "r") as file:
        for record in csv.DictReader(file):
            result.append(record)
    return result