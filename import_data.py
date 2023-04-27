import mysql.connector
import pandas as pd

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()

#Create the DB (if not already exists)
mycursor.execute("CREATE DATABASE IF NOT EXISTS NBA2K20")

#Create the table for the csv data (if not exists)
mycursor.execute("""
  CREATE TABLE IF NOT EXISTS NBA2K20.Clash_Unit (
    full_name VARCHAR(30) NOT NULL,
    rating INTEGER,
    jersey VARCHAR(30),
    team VARCHAR(30),
    position VARCHAR(30),
    b_day DATE(30),
    height VARCHAR(30),
    weight VARCHAR(30),
    salary VARCHAR(30),
    country VARCHAR(30),
    draft_year
    draft_round
    draft_peak 
    college VARCHAR(30),
    version VARCHAR(30),
    PRIMARY KEY (Unit)
  );""")

#Delete data from the table Clsh_Unit
mycursor.execute("DELETE FROM CLASH_ROYALE.Clash_Unit")
mydb.commit()

#Read data from a csv file
clash_data = pd.read_csv('./cr-unit-attributes.csv', index_col=False, delimiter = ',')
clash_data = clash_data.fillna('Null')
print(clash_data.head(20))

#Fill the table
for i,row in clash_data.iterrows():
    cursor = mydb.cursor()
    #here %S means string values 
    sql = "INSERT INTO CLASH_ROYALE.Clash_Unit VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Record inserted")
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)