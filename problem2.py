#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"
int1 = float(input("please enter an int and I'll say if it's an intiger: "))
if int1 == int(int1):
    print(f"{int1} is an intager")
else:
    print(f"{int1} is not an intiger")