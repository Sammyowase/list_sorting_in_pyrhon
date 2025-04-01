#step one: Ccreate an empty list

my_list = []

#step two: Append elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#step three: Insert 15 at the second position(index 1)

my_list.insert(1, 15)

#step four: Extend my_list with another list [50, 60, 70]
my_list.extend([50, 60, 70])

#step five: Remove the last element from my_list
my_list.pop()

#step six: Sort my_list in ascending order
my_list.sort()

#step seven: Find and print the index of value 30
index_of_30 = my_list.index(30)
print("Index of #0:", index_of_30)

# Print final list
print("Final my_list:", my_list)

#finish
