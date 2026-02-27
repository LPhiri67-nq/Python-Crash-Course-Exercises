# Chapter 4: Working with Lists

# Tuples

# When compared with lists, tuples are simple data structures.
# Use them when you want to store a set of values...
# ...that should not be changed throughout the life of a program.

# Exercise 4-13: Buffet

# A buffet-style restaurant offers only five basic foods.
# Think of five simple foods, and store them in a tuple
buffet_food_options = ("chicken salad", "beef steak","lasagna", "potato wedges", "rice")

# Use a for loop to print each food the restaurant offers.

# Note: A method is an action that Python can perform on a piece of data.
# The dot (.) after name in name.title()...
# ...tells Python to make the title() method act on the variable name.

for food in buffet_food_options:
    print(food.title())

# Try to modify one of the items, and make sure that Python rejects the change.
buffet_food_options.append("casserole")

# The restaurant changes its menu, replacing two of the items with different foods.
# Add a line that rewrites the tuple,...
# ...and then use a for loop to print each of the items on the revised menu.

buffet_food_options = ("chicken salad", "pork steak","lasagna", "sweet potato fries", "rice")

for food_2 in buffet_food_options:
    print(food_2.title())

