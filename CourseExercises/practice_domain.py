# Python EXTRA Exercises
from unittest import skip

# Exercise 1: Arithmetic Product and Conditional Logic

# Problem: Write a Python function that accepts two integer numbers. If the product of the two numbers is less
# than or equal to 1000, return their product; otherwise, return their sum.

# Purpose: Learn basic control flow and the use of if-else statements.
# Understand how code decisions change output based on a mathematical threshold.


number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter a second number: "))
product_of_two_numbers = number_1 * number_2
sum_of_two_numbers = number_1 + number_2

if product_of_two_numbers <= 1000:
    print("The product of two numbers is: " + str(product_of_two_numbers))
else:
    print("The sum of two numbers is: "+ str(sum_of_two_numbers))

# Exercise 2: Cumulative sum of a Range

# Problem: Iterate through the first 10 numbers (0-9). In each iteration, print the current number, the previous number, and their sum.

for number in range(0, 10):
    if number == 0:
        print(f" Current number: {number}, Previous Number: {number}, Sum: {number + number}")
    else:
        print(f" Current number: {number}, Previous Number: {number-1}, Sum: {number + (number-1)}")

# Alternatively:

previous_num = 0

for number in range(0, 10):
    sum_2 = number + previous_num

    print(f" Current number: {number}, Previous Number: {previous_num}, Sum: {sum_2}")
    # Update previous_num for the next iteration
    # Shifts the current value into the "memory" slot for the next cycle of the loop.
    previous_num = number


# Exercise 3: String Indexing and Even slicing

# Practice Problem: Display only those characters which are present at an index number in given string.

# Purpose: Understand how data is stored in memory using zero-based indexing.
# In most languages, the first character is at position 0, the second at 1, and so on.
# Mastering indexing is vital for data parsing.

string_example = "pynative"


# Printing only even index chars
# Method: Using a for loop - will process the resulting subset of characters individually.

for index in range(0, 7):
    if index % 2 == 0:
        print(string_example[index])


# Alternatively Solution #2:

for index in range(0, 9, 2):
    print(string_example[index])


# Alternatively Solution #3:

print("Original String is ", string_example)

# Method: Using list slicing
# Format: [start:stop:step]

even_chars = string_example[0::2]

for char in even_chars:
    print(char)


# A custom input string
# Accept input string from a user

string_example_2 = input("Enter a string: ")
print("Original String: " + string_example_2)

# Get the length of a string
length_of_string = len(string_example_2)

for index in range(0, length_of_string - 1, 2):
    print(f"Index position: {index}, Letter: {string_example_2[index]}")


# Exercise 4: String Slicing and Substring Removal

# Problem: Write a function to remove characters from a string starting from index 0 up to n and a new string.

# Purpose: This exercise demonstrates how to truncate data strings, a common data-cleaning task.

sample_string = input("Enter a string: ")


# Exercise 5: Variable Swapping (The In-pace Method)

# Problem: Write a program to swap the values of two variables, a and b, without using a third temporary variable
# Purpose: This exercise will help you learn about memory efficiency and Python's special tuple unpacking feature.
# In other languages like C or Java, you need a temporary variable to swap values safely.
# In Python, you can swap values in one line without risking data loss.


a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

print(f" Before swap a = {a}, b = {b}")

if a == b:
    print(f" After swap a = {a}, b = {a}")
else:
    print(f" After swap a = {b}, b = {a}")


# Alternatively:


# Simultaneous assignment (Tuple Unpacking)
a, b = b, a

print(f" After swap a = {a}, b = {b}")

# Simultaneous Evaluation: Python evaluates the entire right side (b, a) first, essentially holding both values...
#...essentially holding both values in a temporary hidden structure (a tuple).

# Assignment: It then unpacks those values into the variables on the left.
# This prevents the values of a from being overwritten by 'b' before its original value can be moved.

#Clean code: This eliminates the need for three lines of code and an extra "temp" variable, making the script more readable.


# Exercise 6: Calculating Factorial with a Loop

# Problem: Write a program that calculates the factorial of a given number (e.g., 5!) using a for loop.
# Purpose: This exercise explores "Mathematical Accumulation." A factorial (e.g., 5! = 5*4*3*2*1) requires you...
#...to maintain a running product across multiple iterations, which is a core pattern in scientific computing.

input_number = int(input("Enter a number to calculate its factorial: "))

size = len(str(input_number))

for integer in range(1, size + 1):
    factorial = input_number ** integer
















