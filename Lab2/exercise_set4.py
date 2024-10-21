"""Exercise Set 4:  Pandas & Matplotlib Exercises"""

import numpy as np
#import matplotlib as plt
import matplotlib.pyplot as plt
import pandas as pd

# Load the sales data CSV file
data = pd.read_csv('sales_data.csv')

# Let's print the data to ensure it's loaded correctly
print(data)

# ex1
def exercise1():
    # Extract the month number and total profit columns
    months = data['month_number']
    total_profit = data['total_profit']

    # Create a line plot
    plt.plot(months, total_profit)

    # Labeling the graph
    plt.xlabel('Month Number')
    plt.ylabel('Total Profit')
    plt.title('Total Profit of all Months')

    # Show the plot
    plt.show()


# ex2
def exercise2():
    # Extract the month number and total profit columns
    months = data['month_number']
    total_profit = data['total_profit']

    # Create a styled line plot
    plt.plot(months, total_profit, label='Profit data of last year', color='r', marker='o', markerfacecolor='k',
             linestyle='--', linewidth=3)

    # Labeling the graph
    plt.xlabel('Month Number')
    plt.ylabel('Total Profit')
    plt.title('Styled Total Profit of all Months')

    # Add a legend
    plt.legend()

    # Show the plot
    plt.show()


# ex3
def exercise3():
    # Extract the month number and all product columns
    months = data['month_number']

    # Create multiline plot for each product
    plt.plot(months, data['facecream'], label='Face Cream Sales', marker='o')
    plt.plot(months, data['facewash'], label='Face Wash Sales', marker='o')
    plt.plot(months, data['toothpaste'], label='Toothpaste Sales', marker='o')
    plt.plot(months, data['bathingsoap'], label='Bathing Soap Sales', marker='o')
    plt.plot(months, data['shampoo'], label='Shampoo Sales', marker='o')
    plt.plot(months, data['moisturizer'], label='Moisturizer Sales', marker='o')

    # Labeling the graph
    plt.xlabel('Month Number')
    plt.ylabel('Sales Units')
    plt.title('Sales Data of all Products')

    # Add a legend
    plt.legend()

    # Show the plot
    plt.show()


# ex4
def exercise4():
    # Extract the month number and toothpaste columns
    months = data['month_number']
    toothpaste_sales = data['toothpaste']

    # Create a scatter plot
    plt.scatter(months, toothpaste_sales, label='Toothpaste Sales', color='b')

    # Labeling the graph
    plt.xlabel('Month Number')
    plt.ylabel('Toothpaste Sales Units')
    plt.title('Toothpaste Sales Data of all Months')

    # Show the plot
    plt.show()


# ex5
def exercise5():
    # Extract the month number and bathing soap columns
    months = data['month_number']
    soap_sales = data['bathingsoap']

    # Create a bar chart
    plt.bar(months, soap_sales, label='Bathing Soap Sales', color='g')

    # Labeling the graph
    plt.xlabel('Month Number')
    plt.ylabel('Bathing Soap Sales Units')
    plt.title('Bathing Soap Sales Data of all Months')

    # Save the figure
    plt.savefig('bathing_soap_sales.png')

    # Show the plot
    plt.show()


# ex6
def exercise6():
    # Extract the total profit column
    total_profit = data['total_profit']

    # Create a histogram
    plt.hist(total_profit, bins=5, color='purple', edgecolor='black')

    # Labeling the graph
    plt.xlabel('Profit Range')
    plt.ylabel('Frequency')
    plt.title('Profit Ranges Distribution')

    # Show the plot
    plt.show()


# ex7
def exercise7():
    # Extract the month number, bathing soap, and facewash columns
    months = data['month_number']
    soap_sales = data['bathingsoap']
    facewash_sales = data['facewash']

    # Create subplots
    plt.subplot(2, 1, 1)
    plt.plot(months, soap_sales, label='Bathing Soap Sales', color='b', marker='o')
    plt.title('Bathing Soap Sales Data')
    plt.xlabel('Month Number')
    plt.ylabel('Sales Units')

    plt.subplot(2, 1, 2)
    plt.plot(months, facewash_sales, label='Facewash Sales', color='r', marker='o')
    plt.title('Facewash Sales Data')
    plt.xlabel('Month Number')
    plt.ylabel('Sales Units')

    # Adjust layout
    plt.tight_layout()

    # Show the plot
    plt.show()


if __name__ == "__main__":
    print("EXERCISE SET 4: Pandas & Matplotlib Exercises")

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
