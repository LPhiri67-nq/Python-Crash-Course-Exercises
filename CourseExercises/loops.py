# Working with Lists - Chapter 4
from CourseExercises.data_structures import favourite_movies

# Looping Through an Entire List

# Looping allows you take the same action, or set of actions, with every item in a list.


# For Loops

# Exercise 4.1: Pizzas
# Think of at least three kinds of your favorite pizza.
# Store these pizza names in a list, and then use a for loop to print the name of each pizza.

favourite_pizzas = ["Hawaiian", "Chicken Supreme", "Pepperoni"]

for pizza in favourite_pizzas:
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


# Working with Part of a list

# Slices
# Create a list of items, and add several lines to the end of the program that do the following:

# 1.) Print the message " The first three items in the list are: ".
# Then use a slice to print the first three items from that program's list.

# List reference: reptiles

reptiles_2 = ["Crocodile", "Snakes", "Worm Lizard", "Tortoise", "Caimans", "Gavialis", "Lizards"]

print("The first three items in the list are: ")
print(reptiles_2[:3])



# 2.) Print the message " Three items from the middle of the list are: "
# Then use a slice to print three items from the middle of the list.
print("Three items from the middle of the list are: ")
print(reptiles_2[2:5])


# 3.) Print the message " The last three items in the list are: "
# Then use a slice to print the last three items in the list.
print("The last three items in the list are: ")
print(reptiles_2[4:])




# Exercise 4-11: My Pizzas, Your Pizzas: Start with your program from Exercise 4-1

# Make a copy of the list pizzas, and call it friend_pizzas.

friend_pizzas = favourite_pizzas[:]

# Add a new pizza to the original list.

favourite_pizzas.append("Triple Cheese")

# Add a different pizza to the list friend_pizzas

friend_pizzas.append("Margarita")

# Prove that you have two separate lists.
# Print the message " My favourite pizzas are: "

print("My favourite pizzas are: ")
print(favourite_pizzas)

# Print the message " My friend’s favorite pizzas are: "
print("\nMy friend’s favorite pizzas are: ")
print(f"{friend_pizzas}\n")

# Use a for loop to print the second list.

for pizza in friend_pizzas:
    print(pizza)



#  Exercise 4-12. More Loops
#  All versions of "foods.py" in the chapter section have avoided using for loops when printing, to save space.
#  Choose a version of "foods.py", and write two for loops to print each list of foods

my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods[:]

my_foods.insert(1, "spaghetti")
friend_foods.append("cheese cake")


for food in my_foods:
    print("My favourite food is: " + food + "\n")

for food_2 in friend_foods:
    print("\nMy friend's favourite food is: " + food_2)
