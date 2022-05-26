print("This program checks out whether an year is a leap year or not.")

#User inputs year
year = int(input("Enter the year you want to check: "))

#To check divisbilty, we use '%' operator because it gives us the remainder upon division
#If remainder is 0, the number will be divisble by the number given by us

"""First we'll check for 400, as number divisible by 400 will also be divisible by 100 and 4,
therefore all conditions will be fulfilled and it will be a leap year"""
""" Next we check for 100, year will not be a leap year if it is not divisible by 400 and divisible
by 100"""
"""At last, if year is not divisible by both 100 and 400, we check divisibilty by 4"""

divisible_by_400 = year % 400

divisible_by_100 = year % 100

divisible_by_4 = year % 4

if divisible_by_400 == 0:
    print(year, "IS A LEAP YEAR")
    
elif divisible_by_100 == 0:
    print(year, "IS NOT A LEAP YEAR")
    
elif divisible_by_4 == 0:
    print(year, "IS A LEAP YEAR")
    
else:
    print(year, "IS NOT A LEAP YEAR")    