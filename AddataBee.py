import sqlite3

connection=sqlite3.connect("C:/Hospital/Bee.db")

c=connection.cursor()

print("Add data\n")

idmedicine = str(input('Please enter the idmedicine: '))
namemedicine = str(input('Please enter the namemedicine: '))
typemedicine = str(input('Please enter the typemedicine: '))
size = str(input('Please enter the size: '))
usage = str(input('Please enter the usage: '))
cure = str(input('Please enter the cure: '))

print(idmedicine,namemedicine,typemedicine,size,usage,cure)

c.execute(''' INSERT INTO Hospitals(idmedicine,namemedicine,typemedicine,size,usage,cure)
				VALUES(?,?,?,?,?,?) ''',
				(idmedicine,namemedicine,typemedicine,size,usage,cure))

connection.commit()
connection.close()
