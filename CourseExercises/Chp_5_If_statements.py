# Chapter 5: If statements

# Exercise 5-1: Conditional Tests Write a series of conditional tests.

# Print a statement describing each test...
# ...and your prediction for the results of each test.

# Look closely at your results,...
# ...and make sure you understand why each line evaluates to True or False.

# Create at least 10 tests.
# Have at least 5 tests evaluate to True and another 5 tests evaluate to False.

animal = "Tiger"

print("Is animal == 'tiger'? My prediction is No.")
print(animal == "tiger")

print("\n Is animal.lower() == tiger? My prediction is Yes.")
print(animal.lower() == "tiger")

print("\nIs animal != 'tiger'? My prediction is Yes.")
print(animal != "tiger")

animal = "turtle"

print("\nIs animal.upper() == 'turtle'? My prediction is No.")
print(animal.upper() == "turtle")

print("\nIs animal != 'turtle'? My prediction is No.")
print(animal != "turtle")

print("\nIs animal == 'tiger'? My prediction is No.")
print(animal == "tiger")


# Numerical Comparisons

my_Fathers_age = 33

print("\nIs my_Fathers_age < 40? My prediction is Yes.")
print(my_Fathers_age < 40)

print("\nIs my_Fathers_age > 40? My prediction is No.")
print(my_Fathers_age > 40)

print("\nIs my_Fathers_age >= 33? My prediction is Yes. ")
print(my_Fathers_age >= 33)


# Checking Multiple Conditions

my_sisters_age = 13
my_age = 19

print('''\nIs my_sisters_age < my_age and my_sisters_age > my_Fathers_age? 
      My prediction is No.''')
print(my_sisters_age < my_age and my_sisters_age > my_Fathers_age)


print('''\nIs my_sisters_age < my_age or my_sisters_age > my_Fathers_age? 
      My prediction is Yes.''')
print(my_sisters_age < my_age or my_sisters_age > my_Fathers_age)

print('''\nIs my_sisters_age <= my_age and my_sisters_age != my_Fathers_age? 
      My prediction is Yes.''')
print(my_sisters_age <= my_age and my_sisters_age != my_Fathers_age)


# Exercise 5-2: More Conditional Tests
# You don’t have to limit the number of tests you create to 10.
# Have at least one True and one False result for each of the following:

# Tests for equality and inequality with strings

fabric = "polyester"

if fabric == 'polyester':
    print("\nPolyester sweaters are out of stock.")
else:
    print("\nCotton sweaters and more are available at discounts of up to 50%.")

fabric = "Satin"

if fabric != "Satin":
    print("\nAsk Jennie to buy denim jeans.")
else:
    print("\nAsk Jennie to buy the latest trending satin dress!")


# Tests using the lower() method

animal_3 = "Giraffe"

if animal_3.lower() == "giraffe":
    print("\nThere are no adult giraffes in the Zambezi Zoo.")
else:
    print("\nVisit the auditorium, to see the oldest living Giraffe in the Zambezi Zoo.")

# Numerical tests involving equality and inequality,...
# ...greater than and less than, greater than or equal to...
# ...and less than or equal to...
# ...Tests using the "and" keyword and the "or" keyword.

numbers_from_0_to_34 = list(range(34))

sum_of_numbers = sum(numbers_from_0_to_34)

# Checks is the sum is greater or less than 100.
if sum_of_numbers >= 100:
    print(sum_of_numbers >= 100)
else:
    print("\nThe sum of numbers between 0 to 34 is than 100.")

# Checks is a positive number.
if 0 < sum_of_numbers < 100:
    print(f"\nThe sum of numbers between 0 to 34 is {sum_of_numbers}.")
else:
    print("\nThe sum of the numbers in the range is a negative number.")

# Checks if the sum is greater than 100 and is an even number.
if sum_of_numbers >= 100 and sum_of_numbers % 2 == 0:
    print('''\nThe sum of numbers between 0 to 34 
          is less than 100 and is an odd number.''')
else:
    print('''\nThe sum of numbers between 0 to 34 "
          is less than 100 and is an odd number.''')

# Checks if the sum is a multiple of 10 or 2.

if sum_of_numbers != 100 or sum_of_numbers == 200:
    print("The sum is a not multiple of 10, but it is a multiple of 2.")
else:
    print("The sum is not divisible by 10 or by 2.")

# Test whether an item is in a list

list_of_numbers = list(range(2, 40, 2))

if 23 in list_of_numbers:
    print("The number 23 is in the list of numbers.")
else:
    print("The number 23 is not in the list of numbers.")

# Test whether an item is not in a list

list_of_students = ["Jeremy", "Alice", "Connor"]

reported_Absentees = ["Emily", "Alice"]

if reported_Absentees not in list_of_students:
    print("There's an imposter in the classroom.")
else:
    print("Record student attendance as normal.")