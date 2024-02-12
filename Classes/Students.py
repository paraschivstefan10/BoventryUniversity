
###############################################

#Author : Stefan-Cristian Paraschiv
#Student_ID_No : 12395817
#Email : paraschivs@coventry.ac.uk
#Project : School Database Project

################################################

from .Humans import Humans #This import method allows the code to inherit from Humans class

from .Humans import Humans #This import method allows the code to inherit from Humans class

class Students(Humans):
	def __init__(self, Human_Title, Human_Name, Student_ID_No, Address, Telephone_Number, Email, Date_Enrolled, Graduation_Date):
		super().__init__(Human_Title, Human_Name, Address, Telephone_Number, Email)
		self.Human_Title = Human_Title
		self.Human_Name = Human_Name
		self.Address = Address
		self.Telephone_Number = Telephone_Number
		self.Email = Email
		self.Student_ID_No = Student_ID_No
		self.Date_Enrolled = Date_Enrolled
		self.Graduation_Date = Graduation_Date
		
		
	def print_student_details(self):
		print(" You have added: Student ID Number: " ,self.Student_ID_No, "Student Title :", self.Human_Title, "Student Name: ", self.Human_Name, "Address: ", self.Address, "Telephone Number: ", self.Telephone_Number, "Email: ", self.Email, "Graduation_Date: ", self.Graduation_Date) 

	def print_all_students_details(cursor,connection):
		cursor.execute("SELECT * FROM Students")
		print(cursor.fetchall())
		connection.commit()

	def add_new_student(self,cursor,connection):
		cursor.execute("INSERT INTO Students (Student_ID_No, Student_Name, Address, Telephone, Email, Date_Enrolled, Graduation_Date) VALUES (?,?,?,?,?,?,?)", (self.Student_ID_No, self.Human_Name, self.Address, self.Telephone_Number, self.Email, self.Date_Enrolled, self.Graduation_Date))
		connection.commit()
		print('Student Added Successfully')

	def update_student(Student_ID_No, field_to_update, new_value, cursor, connection):
		cursor.execute(f"UPDATE Students SET {field_to_update} = ? WHERE Student_ID_No = ?", (new_value, Student_ID_No))
		connection.commit()
		print('Student Updated Successfully')

	def delete_student(StudentID,cursor,connection):
		cursor.execute("DELETE FROM StudentsCoursesRegistraions WHERE StudentID = ?", (StudentID,))
		connection.commit()
		print('Student Deleted Successfully')		

#def create_tables():
#	cursor.execute('''CREATE TABLE IF NOT EXISTS StudentsCoursesRegistraions (
#						StudentID	INTEGER PRIMARY KEY,
#						StudentName	TEXT,
#						CourseID	INTEGER,
#						Course_Details	TEXT,
#						TeacherID	INTEGER,
#						Teacher_name	TEXT,
#						Registration_Date	TEXT)''')
	#connection.commit()



