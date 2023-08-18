from prettytable import PrettyTable
import sqlite3
connection=sqlite3.connect("C:/Hospital/Bee.db",timeout=10)
c=connection.cursor()

Editnamemedicine = str(input('Please enter name to be Edited: '))

print("Enter new name\n")

nameDataE = str(input('Please enter the name: '))


c.execute('UPDATE Hospitals  SET namemedicine=? where namemedicine=?',(nameDataE,Editnamemedicine,))

connection.commit()
connection.close()	
	
