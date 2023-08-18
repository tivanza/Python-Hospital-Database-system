from prettytable import PrettyTable
import sqlite3

connection=sqlite3.connect("C:/Hospital/Bee.db",timeout=10)

c=connection.cursor()

idmedicine = str(input('Please enter the idmedicine: '))
namemedicine = str(input('Please enter the namemedicine: '))
typemedicine = str(input('Please enter the typemedicine: '))
size = str(input('Please enter the size: '))
usage = str(input('Please enter the usage: '))
cure = str(input('Please enter the cure: '))

print("Id:"+idmedicine,"| Name:"+namemedicine,"| Type:"+typemedicine,"|Sizs:"+size,"|Usage:"+usage,"|Cure:"+cure)

c.execute(''' INSERT INTO Hospitals(idmedicine,namemedicine,typemedicine,size,usage,cure)
              VALUES(?,?,?,?,?,?) ''',
			  (idmedicine,namemedicine,typemedicine,size,usage,cure))

connection.commit()
connection.close()
