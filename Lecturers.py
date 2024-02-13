###############################################

#Author : Stefan-Cristian Paraschiv
#Student_ID_No : 12395817
#Email : paraschivs@coventry.ac.uk
#Project : School Database Project

################################################

from Classes.Humans import Humans #This import method allows the code to inherit from Humans class

class Lecturers(Humans):
	def __init__(self, Human_Title, Human_Name, Lecturer_ID_No, Lecturer_Course_Teaching, Address,Telephone_Number, Email, Department, Salary):
		super().__init__(Human_Title, Human_Name, Address, Telephone_Number, Email)  #inheritence from humans class
		self.Lecturer_ID_No = Lecturer_ID_No
		self.Human_Title = Human_Title
		self.Human_Name = Human_Name
		self.Lecturer_Course_Teaching = Lecturer_Course_Teaching
		self.Address = Address
		self.Telephone_Number = Telephone_Number
		self.Email = Email
		self.Department = Department
		self.Salary = Salary


	def print_lecturer_details(self):
		print("You have added: Lecturer ID Number: " ,self.Lecturer_ID_No, "\nLecturer Title : ", self.Human_Title, "\nLecturer Name: ", self.Human_Name, "\nAddress: ", self.Address, "\nTelephone Number: ", self.Telephone_Number, "\nEmail: ", self.Email, "\nDepartment: ", self.Department, "\nSalary: ", self.Salary)

	def print_all_lecturers_details(cursor,connection):
		cursor.execute("SELECT * FROM Lecturers")
		print(cursor.fetchall())
		connection.commit()

	def add_new_lecturer(self,cursor,connection):
		cursor.execute("INSERT INTO Lecturers (Lecturer_ID_No, lecturer_Title, Lecturer_Name, Address, Lecturer_Course_Teaching, Telephone_Number, Email, Salary) VALUES (?,?,?,?,?,?,?,?)", (self.Lecturer_ID_No, self.Human_Title, self.Human_Name, self.Address, self.Lecturer_Course_Teaching, self.Telephone_Number, self.Email, self.Salary ))
		connection.commit()
		print('\nLecturer Added Successfully')

	def update_lecturer(Lecturer_ID_No, field_to_update, new_value, cursor, connection):
		cursor.execute(f"UPDATE Lecturers SET {field_to_update} = ? WHERE Lecturer_ID_No = ?", (new_value, Lecturer_ID_No))
		connection.commit()
		print('Lecturer Updated Successfully')

	def delete_Lecturer(cursor,connection,Lecturer_ID_No):
		cursor.execute("DELETE FROM Lecturers WHERE Lecturer_ID_No = ?", (Lecturer_ID_No,))
		connection.commit()
		print('Lecturer Deleted Successfully')		
	
