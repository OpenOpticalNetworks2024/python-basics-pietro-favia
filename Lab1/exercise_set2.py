"""Exercise Set 2: Data Structures"""

import numpy as np
import matplotlib as plt

# Please, remove all the pass in the exercises and substitute them with the expected methods for your functions


# ex1
def exercise1():
    listOne = [3, 6, 9, 12, 15, 18, 21]
    listTwo = [4, 8, 12, 16, 20, 24, 28]

    # Odd index elements from listOne and even index elements from listTwo
    result = listOne[1::2] + listTwo[0::2]

    print("Resulting list:", result)


# ex2
def exercise2():
    sampleList = [34, 54, 67, 89, 11, 43, 94]

    # Remove element at index 4
    element = sampleList.pop(4)

    # Add it to the 2nd position and at the end of the list
    sampleList.insert(2, element)
    sampleList.append(element)

    print("Modified list:", sampleList)


# ex3
def exercise3():
    sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]

    # Split into 3 chunks and reverse each chunk
    chunk_size = len(sampleList) // 3
    chunk1 = sampleList[:chunk_size][::-1]
    chunk2 = sampleList[chunk_size:2 * chunk_size][::-1]
    chunk3 = sampleList[2 * chunk_size:][::-1]

    print("Chunks reversed:", chunk1, chunk2, chunk3)


# ex4
def exercise4():
    sampleList = [11, 45, 8, 11, 23, 45, 23, 45, 89]

    # Create a dictionary to count the occurrences of each element
    count_dict = {}
    for item in sampleList:
        count_dict[item] = count_dict.get(item, 0) + 1

    print("Element counts:", count_dict)


# ex5
def exercise5():
    firstList = [2, 3, 4, 5, 6, 7, 8]
    secondList = [4, 9, 16, 25, 36, 49, 64]

    # Create a set of pairs from both lists
    result_set = set(zip(firstList, secondList))

    print("Resulting set of pairs:", result_set)


# ex6
def exercise6():
    firstSet = {23, 42, 65, 57, 78, 83, 29}
    secondSet = {57, 83, 29, 67, 73, 43, 48}

    # Find the intersection and remove them from firstSet
    intersection = firstSet.intersection(secondSet)
    firstSet.difference_update(intersection)

    print("Updated firstSet after removing intersection:", firstSet)


# ex7
def exercise7():
    firstSet = {57, 83, 29}
    secondSet = {57, 83, 29, 67, 73, 43, 48}

    # Check if firstSet is a subset of secondSet and remove it if true
    if firstSet.issubset(secondSet):
        firstSet.clear()

    print("FirstSet after checking subset:", firstSet)


# ex8
def exercise8():
    rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
    sampleDict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

    # Remove elements from rollNumber if not present in sampleDict values
    rollNumber = [num for num in rollNumber if num in sampleDict.values()]

    print("Filtered roll numbers:", rollNumber)


# ex9
def exercise9():
    speed = {'Jan': 47, 'Feb': 52, 'March': 47, 'April': 44, 'May': 52, 'June': 53, 'July': 54, 'Aug': 44, 'Sept': 54}

    # Get unique values from the dictionary
    unique_values = list(set(speed.values()))

    print("Unique values:", unique_values)


# ex10
def exercise10():
    sampleList = [87, 52, 44, 53, 54, 87, 52, 53]

    # Remove duplicates and create a tuple
    unique_list = list(set(sampleList))
    unique_tuple = tuple(unique_list)

    # Find the minimum and maximum number
    min_value = min(unique_tuple)
    max_value = max(unique_tuple)

    print("Tuple with unique values:", unique_tuple)
    print("Minimum:", min_value)
    print("Maximum:", max_value)


if __name__ == "__main__":
    print("EXERCISE SET 2: Data Structures")

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

    print("EX9")
    exercise9()

    print("EX10")
    exercise10()