# Data Structures: Lists
from traceback import print_tb

from CourseExercises.data_structures import invitees

# Exercise 3.8: Seeing the World

# Think of at least five places in the world you’d like to visit.

# Store the locations in a list. Make sure the list is not in alphabetical order.


places_to_be = ["bali, indonesia", "maldives", "switzerland", "south Korea", "jerusalem, israel"]

# Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
print(places_to_be)

# Use sorted() to print your list in alphabetical order without modifying the actual list.
print(sorted(places_to_be))

# Show that your list is still in its original order by printing it.
print(places_to_be)

# Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
print(sorted(places_to_be, reverse=True))

# Show that your list is still in its original order by printing it again.

print(places_to_be)

# Use reverse() to change the order of your list. Print the list to show that its order has changed.
places_to_be.reverse()
print(places_to_be)

# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
places_to_be.reverse()
print(places_to_be)

# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
places_to_be.sort()

print(places_to_be)

# Use sort() to change your list so it’s stored in reverse-alphabetical order.
places_to_be.sort(reverse=True)

# Print the list to show that its order has changed
print(places_to_be)

# Exercise 3.9: Dinner Guests Continuation
# Working with one of the programs from Exercises 3-4 through 3-7 (pages 41–42).
# Use len() to print a message indicating the number of people you’re inviting to dinner.

print(invitees)

number_of_invitees = len(invitees)

print(number_of_invitees)


# Exercise 3.10: Every Function
# Think of things you could store in a list.
# Write a program that creates a list containing these items and then uses each function introduced at least once.

dream_cars = ["Audi", "Ferrari", "Porsche", "Lamborghini"]

# IN PROGRESS