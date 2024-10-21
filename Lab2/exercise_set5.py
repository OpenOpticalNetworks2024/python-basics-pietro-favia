"""Exercise Set 5:  JSON Exercises"""

import numpy as np
import pandas as pd
import json

# ex1
def exercise1():
    # Read the JSON data from 'states.json' file
    with open('states.json', 'r') as f:
        json_data = json.load(f)  # Load JSON data and convert it to a Python object

    # Print Python object (dictionary)
    print("Python object (converted from JSON):")
    print(json_data)


# ex2
def exercise2():
    # Example Python object (dictionary)
    python_obj = {
        'name': 'David',
        'class': 'I',
        'age': 6
    }

    # Convert Python dictionary to JSON data
    json_data = json.dumps(python_obj)

    # Print the JSON data
    print("JSON data (converted from Python object):")
    print(json_data)


# ex3
def exercise3():
    # Example Python object (dictionary)
    python_obj = {
        'name': 'David',
        'class': 'I',
        'age': 6
    }

    # Convert Python object into a JSON string
    json_string = json.dumps(python_obj)

    # Print the JSON string
    print("JSON string (from Python object):")
    print(json_string)


# ex4
def exercise4():
    # Example Python object (dictionary)
    python_obj = {
        'name': 'David',
        'class': 'I',
        'age': 6
    }

    # Convert Python dictionary to JSON data, sorted by keys, with indentation
    json_data = json.dumps(python_obj, sort_keys=True, indent=4)

    # Print the JSON data
    print("JSON data (sorted by keys, indented):")
    print(json_data)


# ex5
def exercise5():
    # Read the JSON data from 'states.json' file
    with open('states.json', 'r') as f:
        states_data = json.load(f)  # Load JSON data

    # Remove the 'area_codes' field from each state
    for state in states_data['states']:
        if 'area_codes' in state:
            del state['area_codes']

    # Write the modified data to a new JSON file
    with open('states_no_area_codes.json', 'w') as f:
        json.dump(states_data, f, indent=4)

    print("New JSON file created without 'area_codes' field.")


if __name__ == "__main__":
    print("EXERCISE SET 5: Json Exercises")

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
