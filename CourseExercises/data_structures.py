# Numbers ar used quite often in programming to keep score in games, represent data in visualisations, store information in web applications, and so on.
# Python treats numbers in several different ways, depending on how they're used.

# Integers
# Arithemetic operations: In a terminal session, Python simply returns the result of the operation.
# The spacing these operations have no effect on how Python evaluates the expressions.

# Data Structures: List

# Exercise 3.1 : Names
# Store the names of a few of your friends in a list called names. 
# Print each person’s name by accessing each element in the list, one at a time.

names_of_friends = ["Jesus", "Sarah", "Lisa", "Eva", "Lydia"]

print(names_of_friends[0])
print(names_of_friends[1])
print(names_of_friends[2])
print(names_of_friends[3])
print(names_of_friends[4])

# Exercise 3.2 : Greetings

# Start with the list you used in Exercise 3.1...
# ...but instead of just, printing each person’s name, print a message to them.

# The text of each message should be the same, but each message should be personalized with the person’s name.

message = "is my best friend."

print(f"{names_of_friends[0]} {message.removesuffix(".")}" + " for life!")
print(f"{names_of_friends[1]} {message}")
print(f"{names_of_friends[2]} {message}")
print(f"{names_of_friends[3]} {message}")
print(f"{names_of_friends[4]} {message}")

# Exercise 3.3: Your own list

# Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples.
# Use your list to print a series of statements about these items, such as "I would like to own a Honda motorcycle."


favourite_movies = ["Passion of Christ","Captain America: Civil War","Step Up All In","Godzilla","Mamma Mia! Here we go again"]


print(f"{favourite_movies[0]} shares a powerful, life-changing message!")
print(f"{favourite_movies[1]} is my favourite Comic Book Movie adaptation.")
print(f"{favourite_movies[2]} is one of the very few energetic films that ACTUALLY lives up to that title.")
print(f"{favourite_movies[3]} is the my favourite installment in the MonsterVerse")
print(f"{favourite_movies[4]} features one of the best movie soundtracks of all time.")

# Exercise 3.4: Guest List

# If you could invite anyone, living or deceased, to dinner, who would you invite?
# Make a list that includes at least three people you’d like to invite to dinner.
# Then use your list to print a message to each person, inviting them to dinner.

invitees = ["Jesus", "Apostle Paul", "My Beloved Family"]

message =  ''' I'm writing to invite you to my upcoming wedding festival!
I would be delighted to celebrate this wonderful new chapter of my life with you.'''

print("To " +  invitees[0] + ", " + message.lstrip())
print("To " +  invitees[1] + ", " + message.lstrip())
print("To " +  invitees[2] + ", " + message.lstrip())

# Exercise 3.5: Changing the Guest List

# You just heard that one of your guests can’t make the  dinner, so you need to send out a new set of invitations.
# You’ll have to think of someone else to invite.

# Replace Apostle Paul with Peter
# Start with your program from Exercise 3-4.
# Add a print() call at the end of your program, stating the name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list.

print("Announcement: Updated Guest List")
print(f"Unfortunately, due to unprecedented reasons, {invitees[1]} will not be able to attend the wedding.")

# Replacement Guest
invitees[1] = "Peter"


print("To " +  invitees[0] + ", " + message.lstrip())
print("To " +  invitees[1] + ", " + message.lstrip())
print("To " +  invitees[2] + ", " + message.lstrip())


# Exercise 3.6: More Guests

# You just found a bigger dinner table, so now more space is available.
# Think of three more guests to invite to dinner.

# Add a print() call to the end of your program, informing people that you found a bigger table.

print("Announcement: There will be more guests joining us!")
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
#  Print a new set of invitation messages, one for each person in your list.


invitees.insert(0, "Matthew")
invitees.insert(2, "Mark")
invitees.append("Luke")

print("To " +  invitees[0] + ", " + message.lstrip())
print("To " +  invitees[1] + ", " + message.lstrip())
print("To " +  invitees[2] + ", " + message.lstrip())
print("To " +  invitees[3] + ", " + message.lstrip())
print("To " +  invitees[4] + ", " + message.lstrip())
print("To " +  invitees[5] + ", " + message.lstrip())


# Exercise 3.7: Shrinking Guest List
# You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.

# Start with your program from Exercise 3-6.
# Add a new line that prints a message saying that you can invite only two people for dinner.

print("Announcement: I realized that we can only invite 2 people! See updated invitation list below.")

# Use pop() to remove guests from your list one at a time until only two names remain in your list.


# Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
guest_1 = invitees.pop(0)
print(f"Sorry Matthew, I reget to inform you that you have been disinvited. ")

guest_2 = invitees.pop(1)
print(f"Sorry Mark, I reget to inform you that you have been disinvited. ")

guest_3 = invitees.pop(1)
print(f"Sorry Peter, I reget to inform you that you have been disinvited. ")

guest_4 = invitees.pop()
print(f"Sorry Luke, I reget to inform you that you have been disinvited. ")

# Print a message to each of the two people still on your list, letting them know they’re still invited.
print(f"Our Lord Jesus and My Beloved Family are still welcomed to come to the wedding!")

print(invitees)

# Use del to remove the last two names from your list, so you have an empty list.
# Print your list to make sure you actually have an empty list at the end of your program


# del invitees[0]

# print(invitees)

# del invitees[0]

# print(invitees)
