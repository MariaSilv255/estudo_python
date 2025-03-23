import sqlite3
con = sqlite3.connect('db.sqlite3')
sql = con.cursor()

sql.execute("INSERT INTO app1_agenda (nome,telefone) VALUES ('Maria',84987518025)")
sql.execute("INSERT INTO app1_agenda (nome,telefone) VALUES ('Aparecida',40028922)")

con.commit()
con.close()