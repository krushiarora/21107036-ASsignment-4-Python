print("This program gives your grade according to your marks.")


#User inputs marks
secured_marks = float(input("Enter your marks: "))

if secured_marks < 25:
    print("Your grade is F")

elif 25 <= secured_marks < 45:
    print("Your grade is E")
                    
elif 45 <= secured_marks < 50:
    print("Your grade is D")

elif 50 <= secured_marks < 60:
    print("Your grade is C")

elif 60 <= secured_marks < 80:
    print("Your grade is B")

else:
    print("Your grade is A")
    