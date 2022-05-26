#We'll assign a variable in "for loop" to pieces of candy


"""We know pieces of candy in jar are less than 200,
so we can assign a range of 200 to our variable"""

#Then, we apply for "if statement" to give us output that we need

"""Since remainders on division by 5, 6, & 7 are given to us,
we use "%" operator with "and" to fulfil all 3 conditions and give us a number"""

for candy_in_jar in range(200):
    if candy_in_jar % 5 == 2 and candy_in_jar % 6 == 3 and candy_in_jar % 7 == 2:
        print(candy_in_jar)
