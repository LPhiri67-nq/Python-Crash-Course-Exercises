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
    print("Cotton sweaters and more are available at discounts of up to 50%.")

fabric = "Satin"

if fabric != "Satin":
    print("Ask Jennie to buy denim jeans.")
else:
    print("Ask Jennie to buy the latest trending satin dress!")

# Tests using the lower() method



# Numerical tests involving equality and inequality,...
# ...greater than and less than, greater than or equal to...
# ...and less than or equal
# to Tests using the "and" keyword and the "or" keyword.

# Test whether an item is in a list

# Test whether an item is not in a list