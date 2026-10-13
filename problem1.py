#! python3

# Have the user enter a number 
# Determine if the number is an even number. 
# There are many ways to solve this problem
# Hint: One method is to use the modulus, which determines the remainder when two numbers are divided
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is even"
# "the number is odd"

numb = int(input("Please enter a number (int) and I'll say if it's even or odd: "))

if numb % 2 == 0:
    print(f"{numb} is even")
else:
    print(f"{numb} is odd")