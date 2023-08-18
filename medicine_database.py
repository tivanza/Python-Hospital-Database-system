import os
import sqlite3
from prettytable import PrettyTable
from sys import exit

def all():
	os.system('cls')
	def main():		
		print("\n ============================================ Welcome to Simple database program with python Language=============================================\n")
		print("\t\t\t\t\t\t\t  HOSPITAL MANAGEMENT SYSTEM ")
		print("\t\t\t\t\t\t\tThis project was developed by ")
		print("\t\t\t\t\t\t\t1.Mr. Ivan Tendo ")
		print("\t\t\t\t\t\t\t1.Miss Gaewarin Thiantham (Bee) ")
		print("\t\t\t\t\t\t\t2.Miss Soraya   Yongthuam (Jane) ")
		print("\t\t\t\t\t\t\tSubject : Computer Programming ")
		print("\t\t\t\t\t\t\t\t Project Advisor : Ivan Tendo ")
		print(" \n==================================================================================================================================================\n")
	main()
		
	def hospitals():
		os.system('cls')
		hospital()
		
	def hospital():	
		print("\n Choose an option \n\t\t\t\t\t\t\t    A.Add \n\t\t\t\t\t\t\t    B.Show medicine \n\t\t\t\t\t\t\t    C.Search medicine \n\t\t\t\t\t\t\t    D.Edit medicine \n\t\t\t\t\t\t\t    E.Delete medicine \n\t\t\t\t\t\t\t    F.Exit medicine \n\t\t\t\t\t\t\t    G.Addmore \n ")
		print(" \n==================================================================================================================================================\n")
			
	hospital()
		
		
	def Add ():
		os.system('cls')
		connection=sqlite3.connect("C:/Hospital/Bee.db")

		c=connection.cursor()

		c.execute('''CREATE TABLE IF NOT EXISTS Hospitals
				(
				idmedicine integer NOT NULL PRIMARY KEY,
				namemedicine text NOT NULL,
				typemedicine text NOT NULL,
				size text NOT NULL,
				usage text NOT NULL,
				cure text NOT NULL
				)''')
				
		print("Add data\n")

		idmedicine= str(input('Please enter the idmedicine: '))
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

		os.system('cls')
		continues=input("choose M or N \n M. Continue adding \n N. Back to menu \n")
		
		if continues=="M" or continues=="m":
			print("you selected to continue adding\n")
			Addmore()
		
		if continues=="N" or continues=="n":
			print("you selected to go back to the main menu\n")
			all()
		
		
	def Show_medicin():
		os.system('cls')
		print("this is also show data")
		
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
				
		
		continues=input("choose T or S \n T.Exit program \n S.Back to menu \n")
		
		if continues=="T" or continues=="t":
			print("you selected to exit program\n")
			Exit_medicin()
		
		if continues=="S" or continues=="s":
			print("you selected to go back to the main menu\n")
			all()
				
	def Search_medicin():
		os.system('cls')
		print("this is also search data")
		
		connection=sqlite3.connect("C:/Hospital/Bee.db",timeout=10)
		c=connection.cursor()


		searchidmedicine = str(input('Please enter id to be searched: '))

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
				
		continues=input("choose T or S \n T.Exit program \n S.Back to menu \n")
		
		if continues=="T" or continues=="t":
			print("you selected to exit program\n")
			Exit_medicin()
		
		if continues=="S" or continues=="s":
			print("you selected to go back to the main menu\n")
			all()
				
	def Edit_medicin():
		os.system('cls')
		print("this is also edit data")
		connection=sqlite3.connect("C:/Hospital/Bee.db",timeout=10)
		c=connection.cursor()

		Editnamemedicine = str(input('Please enter name to be Edited: '))

		print("Enter new name\n")

		nameDataE = str(input('Please enter the name: '))


		c.execute('UPDATE Hospitals  SET namemedicine=? where namemedicine=?',(nameDataE,Editnamemedicine,))

		connection.commit()
		connection.close()	
		
		
		continues=input("choose T or S \n T.Exit program \n S.Back to menu \n")
		
		if continues=="T" or continues=="t":
			print("you selected to exit program\n")
			Exit_medicin()
		
		if continues=="S" or continues=="s":
			print("you selected to go back to the main menu\n")
			all()
	def Delete_medicin():
		os.system('cls')
		print("this is also delete data")
		
		connection=sqlite3.connect("C:/Hospital/Bee.db",timeout=10)

		c=connection.cursor()
		delidmedicine = str(input('Please enter id to delete: '))
		Hospitals = c.execute('DELETE FROM Hospitals WHERE idmedicine=?', (delidmedicine,))

		connection.commit()
		connection.close()	
		
		continues=input("choose T or S \n T.Exit program \n S.Back to menu \n")
		
		if continues=="T" or continues=="t":
			print("you selected to exit program\n")
			Exit_medicin()
		
		if continues=="S" or continues=="s":
			print("you selected to go back to the main menu\n")
			all()
		
	def Exit_medicin():
		os.system('cls')
		print("this is also exit")
	def Addmore ():
		os.system('cls')
		print("this is also add more data")
		
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
		
		continues=input("choose T or S \n T.Exit program \n S.Back to menu \n")
		
		if continues=="T" or continues=="t":
			print("you selected to exit program\n")
			Exit_medicin()
		
		if continues=="S" or continues=="s":
			print("you selected to go back to the main menu\n")
			all()
			
	def choices():
		choice=input("Please make a selection\n")

		if choice == "A" or choice== "a":
			print ("you selection Add medicine\n")
			Add()
			
		if choice == "B" or choice== "b":
			print ("you selection Show medicine\n")
			Show_medicin()
			
		if choice == "C" or choice== "c":
			print ("you selection Search medicine\n")
			Search_medicin()
			
		if choice == "D" or choice== "d":
			print ("you selection Edit medicine\n")
			Edit_medicin()
			
		if choice == "E" or choice== "e":
			print ("you selection Delete medicine\n")
			Delete_medicin()
			
		if choice == "F" or choice== "f":
			print ("you selection Exit medicine\n")
			Exit_medicin()
			
		if choice == "G" or choice== "g":
			print ("you selection Addmore\n")
			Addmore()
			
			
		if choice != "A" and choice!= "a" and choice != "B" and choice!= "b" and choice != "C" and choice!= "c" and choice != "D" and choice!= "d" and choice != "E" and choice!= "e" and choice != "F" and choice!= "f" and choice != "G" and choice!= "g":
			print ("choice again\n")
			choices()
			
	choices()	
all()	

