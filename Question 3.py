#We will impoprt and the "random" module to generate random integers
#This will generate 2 random numbers and the user will be given the question

import random

print("Multiplication game program for kids.")
print("\nGive the answer of the multipliaction question next to it and the program will tell you whether you got it right or not.")

print("\nThere are 10 questions.")
#Define two random numbers in range 1 to 10

#We will generate new random integers for every question
first_number = random.randint(1, 10)
second_number = random.randint(1, 10)

question_1 = int(input(f"Question 1: {first_number} x {second_number} = "))
if question_1 == round(first_number * second_number):
    print("Right!")
else:
    print("Wrong. The answer is", round(first_number * second_number))    
#-----------------------------------------------------------------------------


first_number = random.randint(1, 10)
second_number = random.randint(1, 10)

question_2 = int(input(f"Question 2: {first_number} x {second_number} = "))
if question_2 == round(first_number * second_number):
    print("Right!")
else:
    print("Wrong. The answer is", round(first_number * second_number))    
#------------------------------------------------------------------------------


first_number = random.randint(1, 10)
second_number = random.randint(1, 10)
    
question_3 = int(input(f"Question 3: {first_number} x {second_number} = "))
if question_3 == round(first_number * second_number):
    print("Right!")
else:
    print("Wrong. The answer is", round(first_number * second_number)) 
#------------------------------------------------------------------------------


first_number = random.randint(1, 10)
second_number = random.randint(1, 10)

question_4 = int(input(f"Question 4: {first_number} x {second_number} = "))
if question_4 == round(first_number * second_number):
    print("Right!")
else:
    print("Wrong. The answer is", round(first_number * second_number))    
#------------------------------------------------------------------------------


first_number = random.randint(1, 10)
second_number = random.randint(1, 10) 
 
question_5 = int(input(f"Question 5: {first_number} x {second_number} = "))
if question_5 == round(first_number * second_number):
    print("Right!")
else:
    print("Wrong. The answer is", round(first_number * second_number))    
#------------------------------------------------------------------------------


first_number = random.randint(1, 10)
second_number = random.randint(1, 10)

question_6 = int(input(f"Question 6: {first_number} x {second_number} = "))
if question_6 == round(first_number * second_number):
    print("Right!")
else:
    print("Wrong. The answer is", round(first_number * second_number))    
#------------------------------------------------------------------------------


first_number = random.randint(1, 10)
second_number = random.randint(1, 10)

question_7 = int(input(f"Question 7: {first_number} x {second_number} = "))
if question_7 == round(first_number * second_number):
    print("Right!")
else:
    print("Wrong. The answer is", round(first_number * second_number))    
#------------------------------------------------------------------------------


first_number = random.randint(1, 10)
second_number = random.randint(1, 10)
 
question_8 = int(input(f"Question 8: {first_number} x {second_number} = "))
if question_8 == round(first_number * second_number):
    print("Right!")
else:
    print("Wrong. The answer is", round(first_number * second_number))        
#------------------------------------------------------------------------------


first_number = random.randint(1, 10)
second_number = random.randint(1, 10)

question_9 = int(input(f"Question 9: {first_number} x {second_number} = "))
if question_9 == round(first_number * second_number):
    print("Right!")
else:
    print("Wrong. The answer is", round(first_number * second_number))        
#------------------------------------------------------------------------------


first_number = random.randint(1, 10)
second_number = random.randint(1, 10)

question_10 = int(input(f"Question 10: {first_number} x {second_number} = "))
if question_10 == round(first_number * second_number):
    print("Right!")
else:
    print("Wrong. The answer is", round(first_number * second_number))    
    