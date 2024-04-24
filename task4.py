import numpy as np

my_numpy_array = np.array([3, 5, 6, 2, 8, 10 ,20, 50])

# Access a specific index from the numpy array

x = my_numpy_array[0]
print(x)

# Starting from the first index 0 up until and NOT including the last element

x = my_numpy_array[:-1]
print(x)

# Broadcasting, altering several values in a numpy array at once

my_numpy_array[0:4] = 7
print(my_numpy_array)

# Let's define a two dimensional numpy array

matrix = np.random.randint(1, 10, (4, 4))
print(matrix)

# Get a row from a mtrix

row1 = matrix[0]
row2 = matrix[1]

# Get one element

elem = matrix[1][1]
print(elem)

#MINI CHALLENGE #4: In the following matrix, replace the last row with 0
matrix_challenge = np.random.randint(-5, 40, (5, 5))
print(matrix_challenge)
print("\n")
matrix_challenge[-1] = 0
print(matrix_challenge)