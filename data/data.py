import sqlite3
import pandas as pd

df = pd.read_csv('data/College-labor-data.csv')

df.columns = df.columns.str.strip()

connection = sqlite3.connect('demo.sqlite3')

df.to_sql("data_2", connection, if_exists='replace', index=False)