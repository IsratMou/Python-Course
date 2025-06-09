# x = 3.14
# y = -4
# z = 5

# result= round(x)
# result=max(x, y, z)
# result = min(x, y, z)
# result = abs(y)
# result = pow(4, 3)
# print(result)


import math

# x = 9.3
# print(math.pi)
# print(math.e)

# # result= math.sqrt(x)
# result = math.ceil(x)
# # result = math.floor(x)
# print(result)


# ----------------------Exercise------------------------

# calculate the circumference,area of a circle, c=2*pi*r

# r = float(input("Enter the radius of the circle: "))

# c = 2 * math.pi * r
# area = math.pi * (r**2)

# print(f"The circumference of the circle with radius {r} is: {round(c, 2)}")
# print(f"Area of circle= {round(area, 2)} cm²")


# ----------------------Exercise------------------------
# calculate c=root(a^2 + b^2)

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))

c = math.sqrt(a**2 + b**2)

print(f"The length of the hypotenuse c is: {round(c, 2)} units")
