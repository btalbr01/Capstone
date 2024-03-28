#This file calls the other python files to run their scrapers and export .csv files
import subprocess
import MySQLdb
import csv
import mysql.connector
import webbrowser

#connective to SQL
host = 'localhost'
user = 'root'
password = ''

schema_name = 'properties'

conn = mysql.connector.connect(host=host, user=user, password=password)

cursor = conn.cursor()

#creates the database if it doesn't already exist
create_schema_query = f'CREATE DATABASE IF NOT EXISTS {schema_name}'

cursor.execute(create_schema_query)

conn.commit()

cursor.close()
conn.close()

#runs zillow.py and realtor.py to make/update their tables
subprocess.run(["python","zillow.py"])
subprocess.run(["python","realtor.py"])

#opens the php file in web browser
webbrowser.open("http://localhost/realty/Database.php")