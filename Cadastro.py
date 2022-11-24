import mysql.connector 

cnx = mysql.connector.connect(user='root',
                              password='',
                              host='localhost',
                              database='cadastro')

cursor = cnx.cursor()

cursor.execute("SHOW TABLES")

for x in cursor:
  print(x)

