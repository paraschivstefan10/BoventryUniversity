
###############################################

#Author : Stefan-Cristian Paraschiv
#Student_ID_No : 12395817
#Email : paraschivs@coventry.ac.uk
#Project : School Database Project

################################################

#from cmath import e
import sqlite3 #This method allows the developer to connect the code to the database and work hand in hand with the database 
#from tabnanny import check 
import time #This import method allows the developer to manipulate the time or print dates etc. 
from Classes.Humans import Humans
from Classes.Students import Students
from Lecturers import Lecturers

#This function was inspired from my lecturer Kelvin Andrew (who now has been resigned), from Boston College approximately 3 years ago (10/2/2024 when this comment has been written).
#With gratidute, I solemnly thank Kelvin from the bottom of my heart for this lines of code. He stated : "Guys, remember this code, you will need it in future"

def get_int_input(input_message):
  while True:
    raw_value = input(f"{input_message}")
    try:                                       #Function that prevents user from typing strings instead of integers
      integer_value=int(raw_value)
      break
    except ValueError:
      print(f"Type Error. Value {raw_value} cannot be converted into int")
    except:
      print("Unkown Error")
  return integer_value

################################################################################

#This function prevent the user to type negative numbers, numbers bigger than 7 digits or numbers less than 7.
#Students and Lecturer MUST contain only 7 digits 

def check_id_length():
    while True:   #keep the function running until the user type a 7 digit id number
        check_id = input("Enter the ID Number (up to 8 digits): ")
        try:
            ID_No= int(check_id)  
            if len(check_id) != 8:
                raise ValueError("The ID Number cannot be bigger than 8 digits.")
            if ID_No < 0:
                raise ValueError("The ID Number must be a positive number.")
            return ID_No
        except ValueError as e:
            print(e)
                

#def check_if_student_exist(Student_ID_No, cursor):
#     cursor.execute("SELECT 1 FROM Students WHERE Student_ID_No = ?", (Student_ID_No,))
#     result = cursor.fetchone()

#     if result is None:
#        print("Student ID does not exist.")
#     else:
#        print("Student ID exists.")

def main_menu():
    while True:   #Loop to keep the application running.
        print(''' Welcome. Please select only using integers the following options:
        \n 
        Type [1] to manage Students \n 
        Type [2] to manage Lecturers \n 
        Type [3] to manage Courses \n 
        Type [4] for enrollment purposes \n ''')
   
        menu_choice = input('Input your choice: ')
    
        if  menu_choice == '1':
        
            print('\n\n You have chosen to manage Students,\n')
            student_main_menu()
        elif menu_choice == '2':
            print("\n\n You have chosen to manage Lecturers")
            lecturer_main_menu()

def student_main_menu():  #For clarity I considered separating main menu's so the reader can identify  
            inside_menu_choice = input('Type [1] to add a new student,\n Type [2] to update an exsiting student,\n Type [3] to delete a student,\n Type [4] to view all students details')
        
            if inside_menu_choice == '1':
             
                 Student_ID_No = check_id_length()
                 Human_Title = input('Enter the title of the Student: \n')
                 Human_Name = input('Enter the name of the Student: \n')
                 Address = input("Enter the Student's address: \n")
                 Date_Enrolled = input("Enter the Enrolment Date: \n")
                 Telephone_Number = get_int_input("Enter the Student's phone number: \n")
                 Email = input("Enter Student's Email: \n")            
                 Graduation_Date = input("Enter Student's Graduation Date \n")
                 s = Students(Human_Title, Human_Name, Student_ID_No, Address, Telephone_Number, Email ,Date_Enrolled, Graduation_Date)
                 s.add_new_student(cursor,connection)
                 s.print_student_details()
                 more_students = get_int_input("Would you like to go back to students main menu? [1] - Yes  [2] - No ")
                 
                 if more_students == 1:
                     print("Thank you. Redirecting to the Student Main Menu in 3 seconds \n")
                     time.sleep(4)   #by using import time, the time can be manipulated, this results in application sending the user back to the main menu after 4 seconds.
                     student_main_menu()
                 else:
                     print("Thank you. Redirecting to the main menu in 3 seconds \n")
                     time.sleep(4)    
                     main_menu()

            elif inside_menu_choice == '2':

              print("You have chosen to edit a Student Information ")
              Student_ID_No = get_int_input("Type the desired Student ID to modify")
              print("Please type one of the following: ")
              choice_update = get_int_input('''
              Type [1] to edit a Student ID Number \n 
              Type [2] to edit Student Name \n
              Type [3] to edit Student Address \n
              Type [4] to edit the Student Telephone Number \n
              Type [5] to edit the Student Email \n
              Type [6] to edit the Student Graduation Date
              ''')

              mapping = {1: 'Student_ID_No',
                     2: 'StudentName',            
                     3: 'Address',
                     4: 'Telephone',
                     5: 'Email',
                     6: 'Graduation_Date',
                     }
              if choice_update in mapping:

                new_value = input(f"Enter the new value for {mapping[choice_update]}: ")
                field_to_update = mapping[choice_update]
                Students.update_student(Student_ID_No, field_to_update, new_value, cursor, connection) 
                
              else:
                print("Re Type your selection")
            
            elif inside_menu_choice == '3':
                #try:
                 Student_ID_No = get_int_input("Type the student nr: ")
                #    check_if_student_exist(cursor, Student_ID_No)
                    
                #except ValueError as e:
                #    print(e)

                 Students.delete_student(cursor,connection, Student_ID_No)
                 delete_more_students = get_int_input("Would you like to go back to students main menu? [1] - Yes  [2] - No ")
                 
                 if delete_more_students == 1:
                     print("Thank you. Redirecting to the Student Main Menu in 3 seconds \n")
                     time.sleep(4)   #by using import time, the time can be manipulated, this results in application sending the user back to the main menu after 4 seconds.
                     student_main_menu()
                 else:
                     print("Thank you. Redirecting to the main menu in 3 seconds \n")
                     time.sleep(4)    
                     main_menu()

            elif inside_menu_choice == '4':

              Students.print_all_students_details(cursor,connection)
            else:
              print('input is not valid')


def lecturer_main_menu():
     inside_menu_choice = input('Type [1] to add a new Lecturer,\n Type [2] to update an exsiting Lecturer,\n Type [3] to delete a Lecturer,\n Type [4] to view all Lecturer details')
        
     if inside_menu_choice == "1":
             
                 Lecturer_ID_No = check_id_length()
                 Human_Title = input('Enter the title of the Lecturer: \n')
                 Human_Name = input('Enter the name of the Lecturer: \n')
                 Lecturer_Course_Teaching= input("Wwhat he teach")
                 Address = input("Enter the Lecturer's address: \n")
                 Telephone_Number = get_int_input("Enter the Lecturer's phone number: \n")         
                 Email = input("Type Lecturer Email")
                 Department = input("Which deaprtment is the Lecturer enrolled into? ")
                 Salary = get_int_input("Type the Lecturer Salary: ")
                 l = Lecturers(Lecturer_ID_No, Human_Title, Human_Name,Lecturer_Course_Teaching,Address, Telephone_Number,Email, Department, Salary )
                 l.add_new_lecturer(cursor,connection)
                 l.print_lecturer_details()
                 more_lecturers = get_int_input("Would you like to go back to lecturer main menu? [1] - Yes  [2] - No ")
                 
                 if more_lecturers == 1:
                     print("Thank you. Redirecting to the Student Main Menu in 3 seconds \n")
                     time.sleep(4)   #by using import time, the time can be manipulated, this results in application sending the user back to the main menu after 4 seconds.
                     student_main_menu()
                 else:
                     print("Thank you. Redirecting to the main menu in 3 seconds \n")
                     time.sleep(4)    
                     main_menu()

def create_tables():
	 cursor.execute('''CREATE TABLE IF NOT EXISTS Lecturers (
						Lecturer_ID_No	INTEGER PRIMARY KEY AUTOINCREMENT,
						lecturer_Title  TEXT,
						Lecturer_Name	TEXT,
						Address        TEXT,
			   Lecturer_Course_Teaching TEXT,
						Telephone_Number     INTEGER,
						Email TEXT
						Department	TEXT,
						Salary	INTEGER
						)''')
         

       
connection = sqlite3.connect('BoventryUniversityDatabase.db')
cursor = connection.cursor()
connection.commit()	
create_tables()
main_menu()
connection.close()

