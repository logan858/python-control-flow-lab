# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

print("Enter the three lengths of a triangle: ")
first_length = input("a: ")
second_length = input("b: ")
third_length = input("c: ")

if(first_length == second_length and first_length == third_length):
    print(f"A triangle with sides of {first_length}, {second_length} & {third_length} is an equalateral triangle.")
elif(first_length != second_length and first_length != third_length and second_length != third_length):
    print(f"A triangle with sides of {first_length}, {second_length} & {third_length} is a scalene triangle.")
else: 
    print(f"A triangle with sides of {first_length}, {second_length} & {third_length} is an isosceles triangle.")
