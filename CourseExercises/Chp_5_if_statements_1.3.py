# Exercise 5-10: Checking Usernames

# Do the following to create a program that simulates...
# ...how websites ensure that everyone has a unique username.

# Make a list of five or more usernames called current_users.
current_users = ["Carlos Lyons", "Kenzie Palacios", "Devon Atkins",
                 "Salem Austin", "Legacy Davila", "Noe Estes"]
current_users_lowercase = [current_user.lower() for current_user in current_users]

# Make another list of five usernames called new_users.
# Make sure one or two of the new usernames are also in the current_users list.

new_users = ["Egypt Pena", "Adelynn Hendricks", "Abby Marshall", "legacy davila"]

# Loop through the new_users list...
# ...to see if each new username has already been used.

# If it has, print a message that the person will need to enter a new username.

# If a username has not been used, print a message saying...
# ...that the username is available.

# Make sure your comparison is case insensitive.

# If 'John' has been used, 'JOHN' should not be accepted.
# To do this, you’ll need to make a copy of current_users...
# ...containing the lowercase versions of all existing users.

for new_user in new_users:
    if new_user in current_users:
        print(f"\n{new_user} already exists. Enter a different username")
    elif new_user.lower() in current_users_lowercase:
        print(f"\n{new_user.lower()} already exists. Enter a different username.")
    else:
        print(f"{new_user} is available.\nWelcome, New User!")

# Exercise 5-11: Ordinal Numbers

# Ordinal numbers indicate their position in a list, such as 1st or 2nd.
# Most ordinal numbers end in th, except 1, 2, and 3.
# Store the numbers 1 through 9 in a list.

numbers_from_1_to_9 = list(range(1,10))
# Loop through the list

# Use an if-elif-else chain inside the loop...
# ...to print the proper ordinal ending for each number.

# Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th",...
# ...and each result should be on a separate line.

ordinal_numbers = []

for number in numbers_from_1_to_9:
    if number == 1:
        print(f"\nThe ordinal ending for the number {number} is 'st")
        ordinal_numbers.append("1st")
    elif number == 2:
        print(f"The ordinal ending for the number {number} is 'nd")
        ordinal_numbers.append("2nd")
    elif number == 3:
        print(f"The ordinal ending for the number {number} is 'rd.")
        ordinal_numbers.append("3rd")
    else:
        print(f"The ordinal ending for the number {number} is 'th")
        ordinal_numbers.append(f"{number}th")

print(f"\n{ordinal_numbers}")

for ordinal in ordinal_numbers:
    print(ordinal)