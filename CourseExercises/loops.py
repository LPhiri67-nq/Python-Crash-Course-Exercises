# For Loops

# Exercise 4.1: Pizzas
# Think of at least three kinds of your favorite pizza.
# Store these pizza names in a list, and then use a for loop to print the name of each pizza.

favorite_pizzas = ["Hawaiian", "Chicken Supreme", "Pepperoni"]

for pizza in favorite_pizzas:
    print(pizza)
# Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza.
# For each pizza, you should have one line of output containing a simple statement like "I like pepperoni pizza."
    print(f"{pizza} pizza is the best family meal you can eat.")
# Add a line at the end of your program, outside the for loop, that states how much you like pizza.
print("Peri Peri Chicken Pizza is my all time favourite!\n")
# The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!

# Exercise 4.2. Animals
# Think of at least three different animals that have a common characteristic.
# Store the names of these animals in a list, and then use a for loop to print out the name of each animal.

reptiles = [ "Lizard", "Crocodile", "Bearded Dragon" ]
for reptile in reptiles:
    # Modify your program to print a statement about each animal, such as "A dog would make a great pet."
    print(f"{reptile}s are cold-blooded vertebrates.")

# Add a line at the end of your program, stating what these animals have in common.
# You could print a sentence, such as "Any of these animals would make a great pet!"
print("All these animals are reptiles.")


# Exercise 4.3: Counting to Twenty
# Use a for loop to print the numbers from 1 to 20, inclusive.

for number in range(1, 21):
    print(number)


# Exercise 4-4. One Million
# Make a list of the numbers from one to one million, and then use a for loop to print the numbers.

for number in range(1, 1_000_001):
    print(number)
# (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)


# Exercise 4.5. Summing a Million
# Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million.
numbers = list(range(1, 1_000_001))

print(max(numbers))
print(min(numbers))
# Also, use the sum() function to see how quickly Python can add a million numbers.
print(sum(numbers))


# Exercise 4.6. Odd Numbers
# Use the third argument of the range() function to make a list of the odd numbers from 1 to 20.
odd_numbers_from_1_to_20 = list(range(1, 20, 2))

# Use a for loop to print each number.
for number in odd_numbers_from_1_to_20:
    print(number)

# Exercise 4-7. Threes
# Make a list of the multiples of 3, from 3 to 30.
# Use a for loop to print the numbers in your list.
multiples_of_3 = list(range(3, 31, 3))
for multiple in multiples_of_3:
    print(multiple)


# Exercise 4.8: Cubes
# A number raised to the third power is called a cube. For example,the cube of 2 is written as 2**3 in Python.
# Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
list_of_cubes = list(range(1, 11))
for value in list_of_cubes:
    cube = value ** 3
    print(cube)

# Exercise 4.9 Cube Comprehension
# Use a list comprehension to generate a list of the first 10 cubes.

cubes = [value ** 3 for value in range(1, 11)]
print(cubes)

