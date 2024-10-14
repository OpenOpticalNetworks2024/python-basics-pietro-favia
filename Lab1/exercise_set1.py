"""Exercise Set 1: Python Basics"""

import numpy as np
import matplotlib as plt


# Please, remove all the pass in the exercises and substitute them with the expected methods for your functions


import numpy as np
import matplotlib as plt


# ex1
def exercise1():
    try:
        a = int(input("Enter first integer number: "))
        b = int(input("Enter second integer number: "))
    except ValueError:
        print('Value is not an integer')
        return

    product = a * b
    if product > 1000:
        return a + b
    else:
        return product


# ex2
def exercise2():
    start = int(input("Enter the starting number of the range: "))
    end = int(input("Enter the ending number of the range: "))

    previous_num = 0
    for i in range(start, end + 1):
        sum_of_numbers = previous_num + i
        print(f"Current number: {i}, Previous number: {previous_num}, Sum: {sum_of_numbers}")
        previous_num = i


# ex3
def exercise3():
    num_list = list(map(int, input("Enter a list of integers separated by space: ").split()))
    return num_list[0] == num_list[-1]


# ex4
def exercise4():
    num_list = list(map(int, input("Enter a list of integers separated by space: ").split()))

    print("Numbers divisible by 5:")
    for num in num_list:
        if num % 5 == 0:
            print(num)


# ex5
def exercise5():
    text = "Emma is a good developer. Emma is also a writer"
    count = text.lower().count("emma")
    return count


# ex6
def exercise6():
    list1 = list(map(int, input("Enter the first list of integers separated by space: ").split()))
    list2 = list(map(int, input("Enter the second list of integers separated by space: ").split()))

    odd_numbers = [x for x in list1 if x % 2 != 0]
    even_numbers = [x for x in list2 if x % 2 == 0]

    third_list = odd_numbers + even_numbers
    return third_list


# ex7
def exercise7():
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")

    middle_index = len(s1) // 2
    new_string = s1[:middle_index] + s2 + s1[middle_index:]
    return new_string


# ex8
def exercise8():
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")

    first_char_s1 = s1[0]
    middle_char_s1 = s1[len(s1) // 2]
    last_char_s1 = s1[-1]

    first_char_s2 = s2[0]
    middle_char_s2 = s2[len(s2) // 2]
    last_char_s2 = s2[-1]

    return first_char_s1 + middle_char_s1 + last_char_s1 + first_char_s2 + middle_char_s2 + last_char_s2


# ex9
def exercise9():
    input_string = input("Enter a string: ")

    lower_case_count = sum(1 for char in input_string if char.islower())
    upper_case_count = sum(1 for char in input_string if char.isupper())
    digit_count = sum(1 for char in input_string if char.isdigit())
    special_char_count = sum(1 for char in input_string if not char.isalnum())

    print(f"Lowercase letters: {lower_case_count}")
    print(f"Uppercase letters: {upper_case_count}")
    print(f"Digits: {digit_count}")
    print(f"Special characters: {special_char_count}")


# ex10
def exercise10():
    input_string = input("Enter a string: ")

    count = input_string.lower().count("usa")
    return count


# ex11
def exercise11():
    input_string = input("Enter a string: ")

    digits = [int(char) for char in input_string if char.isdigit()]

    if digits:
        total_sum = sum(digits)
        average = total_sum / len(digits)
        return total_sum, average
    else:
        return 0, 0


# ex12
def exercise12():
    input_string = input("Enter a string: ")

    char_count = {}

    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char, count in char_count.items():
        print(f"'{char}': {count}")


if __name__ == "__main__":
    print("EXERCISE SET 1")

    print("EX1: Product or Sum")
    print(exercise1())

    print("\nEX2: Sum of current and previous numbers")
    exercise2()

    print("\nEX3: First and last numbers are the same")
    print(exercise3())

    print("\nEX4: Numbers divisible by 5")
    exercise4()

    print("\nEX5: Count occurrences of 'Emma'")
    print(exercise5())

    print("\nEX6: Odd from first list, even from second list")
    print(exercise6())

    print("\nEX7: Append second string in the middle of first string")
    print(exercise7())

    print("\nEX8: New string from first, middle, and last characters")
    print(exercise8())

    print("\nEX9: Count of lower, upper, digits, and special symbols")
    exercise9()

    print("\nEX10: Count occurrences of 'USA'")
    print(exercise10())

    print("\nEX11: Sum and average of digits in the string")
    print(exercise11())

    print("\nEX12: Character frequency count")
    exercise12()
