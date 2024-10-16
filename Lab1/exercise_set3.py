"""Exercise Set 3: Numpy Exercises"""

import numpy as np
import matplotlib as plt

# Please, remove all the pass in the exercises and substitute them with the expected methods for your functions

# ex1
def exercise1():
    # Create a 4x2 integer array
    array = np.random.randint(1, 100, size=(4, 2))

    # Print array attributes
    print("Array:\n", array)
    print("Shape:", array.shape)
    print("Dimensions:", array.ndim)
    print("Item size (bytes):", array.itemsize)
    print("Data type:", array.dtype)


# ex2
def exercise2():
    # Create a 5x2 integer array from 100 to 200 with a step of 10
    array = np.arange(100, 200, 10).reshape(5, 2)

    print("Array:\n", array)


# ex3
def exercise3():
    # Given 2D array
    array = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])

    # Return the third column of each row
    third_column = array[:, 2]

    print("Third column of each row:", third_column)


# ex4
def exercise4():
    # Given 2D array
    array = np.array([[3, 6, 9, 12], [15, 18, 21, 24], [27, 30, 33, 36], [39, 42, 45, 48], [51, 54, 57, 60]])

    # Return the odd rows and even columns
    result = array[::2, ::2]  # Odd rows: [0, 2, 4] and Even columns: [0, 2]

    print("Odd rows and even columns:\n", result)


# ex5
def exercise5():
    # Two given arrays
    array1 = np.array([[5, 6, 9], [21, 18, 27]])
    array2 = np.array([[15, 33, 24], [4, 7, 1]])

    # Add arrays and calculate square root
    result = np.sqrt(array1 + array2)

    print("Array after addition and square root:\n", result)


# ex6
def exercise6():
    # Given array
    array = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

    # Sort the array
    sorted_array = np.sort(array, axis=None).reshape(3, 3)

    print("Sorted array:\n", sorted_array)


# ex7
def exercise7():
    # Given array
    array = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

    # Max of axis 0 (columns) and min of axis 1 (rows)
    max_axis0 = np.max(array, axis=0)
    min_axis1 = np.min(array, axis=1)

    print("Max of axis 0:", max_axis0)
    print("Min of axis 1:", min_axis1)


# ex8
def exercise8():
    # Given array
    array = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
    new_column = np.array([10, 10, 10])

    # Delete second column
    array = np.delete(array, 1, axis=1)

    # Insert new column at index 1
    array = np.insert(array, 1, new_column, axis=1)

    print("Array after column deletion and insertion:\n", array)


if __name__ == "__main__":
    print("EXERCISE SET 3: NumPy Exercises")

    print("EX1")
    exercise1()

    print("EX2")
    exercise2()

    print("EX3")
    exercise3()

    print("EX4")
    exercise4()

    print("EX5")
    exercise5()

    print("EX6")
    exercise6()

    print("EX7")
    exercise7()

    print("EX8")
    exercise8()