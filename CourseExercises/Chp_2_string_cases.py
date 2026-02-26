# Exercise 2.3: Personal Message

# Use a variable to represent a person's name, and then print that person's name, and print a message to that person.
# Your message should be as simple, such as, "Hello Eric, would you like to learn some Python today?"

user_name = input("What is your name?")
print("Hello " + user_name + ", would you like to learn some Python today?")

# Exercise 2.4: Name Cases
# Use a variable to represent a person’s name.
# Then, print that person’s name in lowercase, uppercase, and title case.

print(user_name.lower())
print(user_name.upper())
print(user_name.title())

# Exercise 2.5: Famous Quote

# Find a quote from a famous person you admire. Print the quote and the name of its author.

favourite_quote = ' Apostle Paul once said, "I can do all things through Him who strengthens me" '
print(favourite_quote)

# Exercise 2.6: Famous Quote 2
# Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person.
# Then compose your message and represent it with a new variable called message. Print your message.

famous_person =  "Apostle Paul"
message = ' "I can do all things through him who strengthens me" '

print(famous_person + " once said, " + message)

# Exercise 2.7: Stripping Names
# Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name.
# Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.

# Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

person_names = "\tEmily Jones\t"
person_names_2 = ' Jonathan Jones '
print(person_names)

print(person_names_2.lstrip())
print(person_names_2.rstrip())
print(person_names_2.strip())

# Exercise 2.8: File Extensions
# Python has a removesuffix() method that works exactly like removeprefix().
# Assign the value 'python_notes.txt' to a variable called filename.
# Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.

filename = 'python_note.txt'
print(filename.removesuffix('.txt'))

