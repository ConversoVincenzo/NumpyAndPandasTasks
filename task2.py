import numpy as np

# Task 2
# "rand()" uniform distribution between 0 and 1

x = np.random.rand(20)
print(x)

#create a matrix with rand numbers

x = np.random.rand(3, 3)
print(x)

# "randint" is used to generate random integers between upper and lower bounds

x = np.random.randint(1,50)
print(x)


# "randint" can be used to generate random a certain number of random integers as follow

x = np.random.randint(1, 100, 15)
print(x)

# np.arange creates an evenly spaced values within a given interval

x = np.arange(1, 50)
print(x)

# create a diagonal of ones and zeros everywhere else

x = np.eye(7)
print(x)

# Matriz of ones

x = np.ones((7, 7))
print(x)

# Arrays of zeros

x = np.zeros(8)
print(x)

# Mini Challenge 2, Write a code that takes a positive integer from the user and creates a 1x10 array with random numbers ranging from 0 to the input(Not including)

while True:
    x = (int)(input("Insert a positive integer number:"))
    if x > 0:
        break
    else:
        print("incorrect input")
result = np.random.randint(0, x, 10)
print(result)