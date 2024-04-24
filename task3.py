import numpy as np

# np.arange() returns an evenly spaced values withing a given interval

x = np.arange(1, 10)
print(x)

y = np.arange(1, 10)
print(y)

sum = x+y
print(sum)

squared = x**2
print(squared)

sqrt = np.sqrt(squared)
print(sqrt)

z = np.exp(y)
print(z)

# Challenge 3 Given X and Y (arrays) obtain distance between them

x = np.array([5, 7, 20])
y = np.array([9, 15, 4])

distance = np.sqrt(x**2 + y**2)

print(distance)