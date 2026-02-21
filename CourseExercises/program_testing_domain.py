name_of_cars_from_a_to_c = ["Abarth", "Acura", "Bugatti", "BMW", "Buick", "Cadillac"]
name_of_cars_from_d_to_g = ["Dacia", "Dodge", "Ferrari", "Fiat", "Great Wall Motors"]

print(name_of_cars_from_a_to_c)
print(name_of_cars_from_d_to_g)

# Merge the lists into one

name_of_cars_from_a_to_g = []

for car in name_of_cars_from_a_to_c:
    name_of_cars_from_a_to_g.append(car)
for car_2 in name_of_cars_from_d_to_g:
    name_of_cars_from_a_to_g.append(car_2)

print(name_of_cars_from_a_to_g)

# Sort the list in reverse-alphabetical order

name_of_cars_from_a_to_g.sort(reverse=True)
print(name_of_cars_from_a_to_g)

# Sorting a list temporarily

print("\nHere is the original list: ")
print(sorted(name_of_cars_from_a_to_g))


print("\nHere is the sorted list: ")
print(name_of_cars_from_a_to_g)

# Reverse the list

print("\nHere is the original list again: ")

name_of_cars_from_a_to_g.reverse()
print(name_of_cars_from_a_to_g)

# How many items are in the list

print(f"Number of elements in the list: {len(name_of_cars_from_a_to_g)}\n")

# Add a new element to the list

new_car = "Chrysler"
name_of_cars_from_a_to_g.append(new_car)
print(f"\nMost requested car brand is Chrysler")
print(f"\nUpdated List: {name_of_cars_from_a_to_g}")

# Sort the list alphabetically

name_of_cars_from_a_to_g.sort()


# remove an element from the list

removed_element = "Dodge"
name_of_cars_from_a_to_g.remove(removed_element)
print(f"\nLeast requested car brand is {removed_element}")
print(f"\nUpdated List: {name_of_cars_from_a_to_g}")


# remove an element by index
removed_element_2 = name_of_cars_from_a_to_g.pop(3)
print(f"\nMy least favourite car brand is {removed_element_2}")
print(f"\nUpdated List: {name_of_cars_from_a_to_g}")



# Print the current number of elements stored in the list

print(f"\nThe number of elements currently stored in the list is {len(name_of_cars_from_a_to_g)}")


# Modify elements in the list

# Replace the element in first index position with the last element in the list

print("\nHere is the original list again: ")
print(name_of_cars_from_a_to_g)


print("\nHere is the new sorted list: ")
temp = " "
temp = name_of_cars_from_a_to_g[0]
name_of_cars_from_a_to_g[0] = name_of_cars_from_a_to_g[-1]
name_of_cars_from_a_to_g[-1] = temp


print(name_of_cars_from_a_to_g)


# Add a new element in index position 3

name_of_cars_from_a_to_g.insert(3, "Audi")
print(f"\nMy favourite car brand is Audi")
print(f"\nUpdated List: {name_of_cars_from_a_to_g}")

# Sort the list alphabetically
name_of_cars_from_a_to_g.sort()

print("\nHere is the sorted list in chronological order: ")
print(name_of_cars_from_a_to_g)
