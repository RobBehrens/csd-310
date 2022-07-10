import mysql.connector
pydb = mysql.connector.connect( 
    user ="pyuser",
    password ="MySQL8IsGreat!",
    host="127.0.0.1",
    database="pysports"
    )

mycursor = pydb.cursor()
mycursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN teams ON player.team_id = teams.team_id;")
myresult = mycursor.fetchall()
print("-- listing all players and their assigned teams in database --")
for x in myresult:
    print(x)