from prettytable import PrettyTable
import sqlite3

connection=sqlite3.connect("C:/Hospital/Bee.db",timeout=10)

c=connection.cursor()
c.execute("select*from Hospitals")
rows = c.fetchall()

row_count=len(rows)
m = PrettyTable(['idmedicine','namemedicine','typemedicine','size','usage','cure'])
i=0
while i<row_count:
	m.add_row([rows[i][0],rows[i][1],rows[i][2],rows[i][3],rows[i][4],rows[i][5]])
	i=i+1
print(m)

row_count=len(rows)
