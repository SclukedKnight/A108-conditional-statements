#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# has a percent difference less than 2%
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"

"""
Example:
Enter one side: 5
Enter a second side: 13
Enter third side: 12
that is a right triangle

Enter one side: 13.01
Enter a second side: 5
Enter third side: 12
that is a right triangle

Enter one side: 5
Enter a second side: 15
Enter third side: 12
that is an obtuse triangle


"""

import math
a = float(input("input side 1: "))
b = float(input("input side 2: "))
c = float(input("input side 3: "))

number = [a, b, c]
number.sort()

a = number[0]
b = number[1]
c = number[2]

right = math.sqrt(a ** 2 + b ** 2)



if right * .98 < c < right * 1.02:
    print("Right triangle, or close enough")
elif right > c ** 2:
    print("Acute trinagle")
elif right < c ** 2:
    print("obstuse triangle")
else:
    print("probable not a triangle")