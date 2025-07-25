'''Exercise
Create a program which asks the user for 3 different numbers. Save each one into
variables a, b and c. Create 3 variables: is_a_max, is_b_max, is_c_max.

is_a_max, is_b_max, is_c_max need to be assigned using a combination of relational and logical operators, this one might be hard but give it a try.

Here is one of them solved. You need to make it work for all of them.'''

a = int(input("type the first number: "))
b = int(input("type the second number: "))
c = int(input("type the third number: "))


is_a_max = a > b and a > c
is_b_max = b > a and b > c
is_c_max = c > a and c > b