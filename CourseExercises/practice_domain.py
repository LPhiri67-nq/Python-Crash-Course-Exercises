# Python EXTRA Exercises

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
                                                                                     
# Problem: Write a program that calculates the factorial of a given number (e.g., 5!)
# Purpose: This exercise explores "Mathematical Accumulation." A factorial (e.g., 5! 
#...to maintain a running product across multiple iterations, which is a core pattern
                                                                                     
                                                                                     
input_number = int(input("Enter a number to calculate its factorial: "))             
                                                                                     
                                                                                     
# FIRST TRIAl                                                                        
factorial = 1                                                                        
                                                                                     
for integer in range(1, input_number):                                               
    product_each_round = factorial * (integer + 1)                                   
    factorial = product_each_round                                                   
print(f"The factorial of {input_number} is {factorial}")                             
                                                                                     
# Loop from 1 to input_number(inclusive)                                             
                                                                                     
# range(1, input_number + 1): Since the end of a range is exclusive, we use + 1 to en
# Each pass of the loop updates the value of 'factorial', building the final result s
for integer in range(1, input_number + 1):                                           
    factorial = factorial * integer                                                  
print(f"The factorial of {input_number} is {factorial}")                             
                                                                                     
                                                                                     
# Exercise 7: List manipulation - Add and Remove                                     
# Problem: Create a list of 5 fruits.                                                
# Add a new fruit to the end of the list, then remove the second fruit (at index 1)  
                                                                                     
# Purpose: This exercise teaches "Dynamic Collection Management".                    
# Lists are rarely static; being able to modify, expand, and prune them is essential 
# ...user lists, or inventory systems.                                               
                                                                                     
                                                                                     
# List of fruits                                                                     
fruits = ["apples", "bananas", "cherry", "date", "elderberry"]                       
print(fruits)                                                                        
                                                                                     
del fruits [1]                                                                       
fruits.append("fig")                                                                 
print (fruits)                                                                       
                                                                                     
                                                                                     
# Exercise String Reversal                                                           
# Problem: Write a program that takes a string and reverses it (e.g., "Python" become
# Purpose: This exercise demonstrates "Sequence Slicing."                            
# Strings in Python are sequences, and mastering the slicing syntax is a powerful sho
# ...that would take 5-10 lines of code in other languages.                          
                                                                                     
                                                                                     
# Reversing using slicing                                                            
                                                                                     
user_input_1 =  input("Enter a word: ")                                              
                                                                                     
reversed_text = user_input_1[: :-1]                                                  
                                                                                     
print (f"Original: {user_input_1}")                                                  
print (f"Reversed: {reversed_text}")                                                 
                                                                                     
                                                                                     
                                                                                     
# Alternative Method:                                                                
                                                                                     
user_input_2 = input("Enter a word: ")                                               
                                                                                     
size = len(user_input_2)                                                             
                                                                                     
reversed_output_list = []                                                            
                                                                                     
for index in range(0, size):                                                         
    reversed_output_list.append(user_input_2[index])                                 
                                                                                     
reversed_output_list.reverse()                                                       
                                                                                     
                                                                                     
final_output =  " "                                                                  
for chars in reversed_output_list:                                                   
    final_output += chars                                                            
                                                                                     
print(f"Original word: {user_input_2}, Reversed: {final_output}")                    
                                                                                     
                                                                                     
                                                                                     
# Exercise 9: Vowel Frequency Counter                                                
                                                                                     
# Problem: Write a program to count the total number of vowels ($a, e. i, o, u$).    
# Purpose: This exercise introduces "Membership Testing".                            
# By checking if a character belongs to a specific group (the vowels), you learn how 
# This is a fundamental step toward building text-analysis tools or spam filters.    
                                                                                     
sentence = input("Enter a sentence: ")                                               
                                                                                     
vowels = "aeiou"                                                                     
                                                                                     
count = 0                                                                            
                                                                                     
for chars in sentence:                                                               
    if chars in vowels:                                                              
        count += 1                                                                   
                                                                                     
print(f"Number of vowels = {count}")                                                 
                                                                                     
# Alternative:                                                                       
sentence_2 = input("Enter a sentence: ")                                             
size = len(sentence)                                                                 
chars_list = []                                                                      
                                                                                     
for index in range(0, size):                                                         
    chars_list.append(sentence[index])                                               
                                                                                     
vowels = ""                                                                          
non_vowel_characters = ""                                                            
                                                                                     
for chars in chars_list:                                                             
    if chars == 'a' or chars == 'e' or chars == 'i' or chars == 'o' or  chars == 'u':
     vowels += chars                                                                 
    else:                                                                            
        non_vowels_characters += chars                                               
                                                                                     
number_of_vowels = len(vowels)                                                       
                                                                                     
print (f"Number of vowels: {number_of_vowels}")                                      
                                                                                     
                                                                                     
# Exercise 10: Finding Extremes (Min/Max) in a List                                  
                                                                                     
# Problem: Given a list of integers, find and print both the largest and the smallest
# Purpose: This exercise explores "Aggregate Functions".                             
# While Python has built-in tools, understanding how to identify extremes is critical
#...to find the range of a dataset before processing it.                             
                                                                                     
# List of numbers                                                                    
                                                                                     
nums = [45, 2, 89, 12, 7]                                                            
max_value = max(nums)                                                                
min_value = min(nums)                                                                
print(f" Largest: {max_value}, Smallest: {min_value}")                               
                                                                                     
                                                                                     
                                                                                                                                                                         
