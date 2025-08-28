my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = [] # Create an empty list to store unique elements, think it as a filter that only accepts the first apperance of each number.
for number in my_list: # Browse all numbers from the source list, goes through it one by one.
    if number not in new_list: #If the number doesn't appear within the new list..., check if it's already in new_list
        new_list.append(number) #...append it here, adds number to new_list if it's not already there.
my_list = new_list[:] # Make a copy of new_list, [:] makes sure it's a copy/new list, not a reference.

print("The list with unique elements only:")
print(my_list)
