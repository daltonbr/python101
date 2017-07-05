#from hs_student import *

#james = HighSchoolStudent("james")

#print(james.get_name_capitalize())

from student import *


typed_id = input("Enter a student id: ")
typed_name = input("Enter a student name: ")
typed_last_name = input("Enter a student last name: ")

new_student = Student(typed_name, typed_last_name, typed_id)

print(new_student)