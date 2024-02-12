
###############################################

#Author : Stefan-Cristian Paraschiv
#Student_ID_No : 12395817
#Email : paraschivs@coventry.ac.uk
#Project : School Database Project

################################################
import sqlite3 #This method allows the developewr to connect the code to the database and work hand in hand with the database 
import time #This import method allows the developer to manipulate the time or print dates etc. 
from Classes.Humans import Humans
from Classes.Students import Students

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
def main_menu():
    while True:
        print(''' Welcome. Please select only using integers the following options:
        \n 
        Type [1] to manage Students \n 
        Type [2] to manage Lecturers \n 
        Type [3] to manage Courses \n 
        Type [4] for enrollment purposes \n ''')
    
        menu_choice = input('Input your choice: ')
    
        if  menu_choice == '1':
        
            print('\n\n You have chosen to manage Students,\n Type [1] to add a new student,\n Type [2] to update an exsiting student,\n Type [3] to delete a student,\n Type [4] to view all students details')
        
            inside_menu_choice = input('Input your choice: ')
        
            if inside_menu_choice == '1':
             
                 Student_ID_No = get_int_input('Please input the Student ID: \n')
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
                s.print_student_details()
              else:
                print("Re Type your selection")

            elif inside_menu_choice == '3':
              Students.delete_student(1,cursor,connection)
            elif inside_menu_choice == '4':
              Students.print_all_students_details(cursor,connection)
            else:
              print('input is not valid')

connection = sqlite3.connect('BoventryUniversityDatabase.db')
cursor = connection.cursor()
#create_tables()
main_menu()
connection.close()

