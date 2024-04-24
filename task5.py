import numpy as np

matrix = np.random.randint(1, 10, (5,5))
print(matrix)

# condition on elements

new_matrix = matrix[ matrix > 7]
print(new_matrix)

#obtain odd elements only

odd_elements = matrix[ matrix % 2 != 0]
print(odd_elements)

# challenge 5 In the following matrix, replace negative elements by 0 and replace odd elements with -2

matrix_challange = np.random.randint(-10, 10, (5,5))
print(matrix_challange)
print("\n")
matrix_challange[ matrix_challange < 0 ] = 0
matrix_challange[ matrix_challange % 2 != 0] = -2
print(matrix_challange)