# Triangles in Maths — Clearer Task

# Write a program that:

# Reads three side lengths a, b, c.

# Checks if a valid triangle can be built
# – all sides must be positive, and the longest < sum of the other two.
# – If not valid, print a message and stop.

# Prints:

# the shortest and longest side,

# the side-length type: equilateral (all equal), isosceles (two equal), or scalene (all different),

# the perimeter,

# the angle type using the Pythagorean relation on the longest side:
# right (c² = a²+b²), obtuse (c² > a²+b²), acute (c² < a²+b²).
# If it’s equilateral, also say equiangular (all angles 60°).

c = int(input("input the largest number no negative numbers: "))
b = int(input("input the smallest number no negative numbers: "))
a =int (input("input the medium number no negative numbers: "))

if c >= a + b:
    print("it is invalid")
elif a == b == c:
    print(f"it is equilateral the peremiter is {a + b + c}")
elif c == b:
    print(f"it is isoscles the peremiter is {a +b + c}")
else:
    print(f"it is scalene the peremiter is {a + b + c}")

if c**2 == a**2+b**2:
    print("it is a right triagle")
elif c**2 > a**2+b**2:
    print("it is obtuse")
elif c**2 < a**2+b**2:
    print("it is acute")
else:
    print("it is equiangular")