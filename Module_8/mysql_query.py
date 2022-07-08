import mysql.connector
pydb = mysql.connector.connect( 
    user ="pyuser",
    password ="MySQL8IsGreat!",
    host="127.0.0.1",
    database="pysports"
    )

mycursor = pydb.cursor()
mycursor.execute("SELECT * FROM player")
myresult = mycursor.fetchall()
print("-- listing all Players in database --")
for x in myresult:
    print(x)
mycursor.execute("SELECT * FROM teams")
myresult = mycursor.fetchall()
print("-- listing all teams in database --")
for x in myresult:
    print(x)