my_first_int=20
my_second_int= 8
result= my_first_int + my_second_int
print(result)

my_first_int=20
my_first_float=8.9
result= my_first_int + my_first_float
print(result)

other_string= "sport"
f_string= f"I like to do {other_string}"

other_string= "run minimal"
second_string= " 5 times a week"
f_string= f"I like to do {other_string  + second_string}"
print(f_string)


username= input("put your username here")
users_last_name= input("put your last name here")
user_age = int(input("Whats your age?: "))
print(f"{username}+{users_last_name}+{user_age}")
if( user_age <= 3):
    print ("the user is a baby")
elif (user_age<=12):
    print ("the user is a child")
elif(user_age<=14):
    print ("the user is a preteen")
elif(user_age<=18):
    print ("the user is a teen")
elif(user_age<=35):
    print ("the user is a young adult")
elif(user_age<=64):
    print ("the user is a adult")
elif(user_age>64):
    print ("ethe user is a senior citizen")
    
    
    import random
secret_number = random .randint(1,10)
attempts_counter= 0
guess_the_number= 0
print("guess the number from 1 to 10")
while guess_the_number != secret_number:
 guess_the_number = int(input("Ienter your number: "))
 attempts_counter = +1
 if guess_the_number< secret_number:
  print("choose another number")
 elif guess_the_number > secret_number:
  print("choose another number")
 else:
  print("correct that was the number")
  
  
  num_1 = int(input("enter your first number: "))
num_2 = int(input("enter your second number: "))
num_3 = int(input("enter your third number: "))
if num_1 > num_2 and num_1 > num_3:
    mayor = num_1
elif num_2 > num_1 and num_2 > num_3:
    mayor = num_2
else:
    mayor = num_3
print(f"the largest number is: {mayor}")


total_grades = 0
note_counter = 1
current_note = 0
number_of_passing_grades = 0
number_of_failed_grades = 0
average_of_falling_grades = 0
average_of_passing_grades = 0
total_grade_average = 0
total_grades = int(input("enter the number of notes: "))
while note_counter <= total_grades:
    print(f"enter note number {note_counter}: ")
    current_note = int(input("> "))
    if current_note < 70:
        number_of_failed_grades += 1
        average_of_falling_grades += current_note
    else:
        number_of_passing_grades+= 1
        average_of_passing_grades += current_note
    total_grade_average += (current_note / total_grades)
    note_counter += 1
if number_of_passing_grades > 0:
    average_of_passing_grades = average_of_passing_grades / number_of_passing_grades
else:
    average_of_passing_grades = 0

if number_of_failed_grades > 0:
    average_of_falling_grades = average_of_falling_grades / number_of_failed_grades
else:
    average_of_falling_grades = 0
print("ResultS")
print(f"number of passing grades: {number_of_passing_grades}")
print(f"Average passing grades: {average_of_passing_grades}")
print(f"number of failed grades: {number_of_failed_grades}")
print(f"Average of failed grades: {average_of_falling_grades}")
print(f"Total grade average: {total_grade_average}")







