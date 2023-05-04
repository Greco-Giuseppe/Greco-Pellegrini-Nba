from flask import render_template
from flask import Flask
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="NBA2K20"
)
mycursor = mydb.cursor()

app = Flask(__name__)


@app.route('/')
def unitList():
    mycursor.execute("SELECT * FROM Clash_Unit")
    myresult = mycursor.fetchall()
    return render_template('clash_units.html', units=myresult)