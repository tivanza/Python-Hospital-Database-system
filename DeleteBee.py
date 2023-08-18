from prettytable import PrettyTable
import sqlite3

connection=sqlite3.connect("C:/Hospital/Bee.db",timeout=10)

c=connection.cursor()
delidmedicine = str(input('Please enter name to delete: '))
Hospitals = c.execute('DELETE FROM Hospitals WHERE idmedicine=?', (delidmedicine,))

connection.commit()
connection.close()	
	
	