from prettytable import PrettyTable
import sqlite3
connection=sqlite3.connect("C:/Hospital/Bee.db",timeout=10)
c=connection.cursor()


searchidmedicine = str(input('Please enter name to be searched: '))

c.execute('select*from Hospitals where idmedicine=?',(searchidmedicine,))
rows = c.fetchall()

row_count=len(rows)
print(row_count)

if row_count<1:
	print("Search doesnt exist\n")

else: 
	m = PrettyTable(['idmedicine','namemedicine','typemedicine','size','usage','cure'])
	m.add_row([rows[0][0],rows[0][1],rows[0][2] ,rows[0][3] ,rows[0][4] ,rows[0][5]])
	print(m)

	for row in rows:
		print(row)