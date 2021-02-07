# 🚨 Don't change the code below 👇
from typing import no_type_check_decorator


student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
number_of_students = 0
total_height = 0
for height in student_heights:
    number_of_students += 1
    total_height += height

print(f"Average Height is {round(total_height/number_of_students)}")

