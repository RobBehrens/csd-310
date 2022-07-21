import mysql.connector
pydb = mysql.connector.connect( 
    user ="pyuser",
    password ="MySQL8IsGreat!",
    host="127.0.0.1",
    database="pysports"
    )
mycursor = pydb.cursor()
mycursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN teams ON player.team_id = teams.team_id")
myresult = mycursor.fetchall()
print("-- listing all players and their assigned teams in database --")
for x in myresult:
    print("player id {} first name {} last name {} team name {}".format(x[0], x[1], x[2], x[3]))
sql = "UPDATE player SET team_id=2 WHERE first_name = 'Jack'"
mycursor.execute(sql)
pydb.commit()
mycursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN teams ON player.team_id = teams.team_id")
myresult = mycursor.fetchall()
print("-- listing all players and their assigned teams in database after update --")
for x in myresult:
    print("player id {} first name {} last name {} team name {}".format(x[0], x[1], x[2], x[3]))
sql = "DELETE FROM player WHERE first_name='Jack'"
mycursor.execute(sql)
pydb.commit()
mycursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN teams ON player.team_id = teams.team_id")
myresult = mycursor.fetchall()
print("-- listing all players and their assigned teams in database after delete --")
for x in myresult:
    print("player id {} first name {} last name {} team name {}".format(x[0], x[1], x[2], x[3]))
sql = "INSERT INTO player (first_name, last_name, team_id) VALUES(%s, %s, %s)"
val = ("jack", "o'neill", 1)

mycursor.execute(sql, val)
pydb.commit()
mycursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN teams ON player.team_id = teams.team_id")
myresult = mycursor.fetchall()
print("-- listing all players and their assigned teams in database after insert--")
for x in myresult:
    print("player id {} first name {} last name {} team name {}".format(x[0], x[1], x[2], x[3]))