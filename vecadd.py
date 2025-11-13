import numpy as np

vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

sum_vector = vector1 + vector2

print("Vector 1:", vector1)
print("Vector 2:", vector2)
print("Sum of vectors:", sum_vector)

sum_vector_func = np.add(vector1, vector2)
print("Sum of vectors (using np.add):", sum_vector_func)

# Keep both improvements (bug fix + dot product)
print("Handled the bug reported by friend")

dot_product = np.dot(vector1, vector2)
dot_product_operator = vector1 @ vector2

print("Dot product (using np.dot):", dot_product)
print("Dot product (using @ operator):", dot_product_operator)

# hello i just modified the file without commiting the changes

