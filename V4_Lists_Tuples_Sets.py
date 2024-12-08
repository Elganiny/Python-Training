# Working with Lists in Python

# Initializing a list of courses
Courses_1 = ['History', 'Math', 'Physics', 'Computer Science']

# Copying the list into a new variable
Courses = Courses_1[:]  # Creates a shallow copy of the list

# Append: Add a new course to the end of the list
Courses.append('Art')
#print(Courses)  # Uncomment to see the result

# Insert: Add a course at a specific index
Courses.insert(0, 'Programming')
#print(Courses)  # Uncomment to see the result

# Extend: Add items from another list to the current list
Courses_2 = ["Programming", "Computer Science"]
Courses.extend(Courses_2)
print("After extending:", Courses)

# Append: Add an entire string to the list (not individual characters)
Courses.append('Programming')
print("After appending 'Programming':", Courses)

# Remove: Delete a specific item from the list
Courses_1 = ['History', 'Math', 'Physics', 'Computer Science']
Courses_1.remove('Computer Science')  # Removes 'Computer Science'
print("After removal:", Courses_1)

# Pop: Remove and return the last item in the list
popped = Courses.pop()
print("Popped item:", popped)  # Outputs the last item that was removed

Courses_1.reverse() # Reverse the list
print("After reverse: ", Courses_1)

# Sort: Sort the list in ascending order
Courses_1.sort()
print("After sorting: ", Courses_1)

num = [1, 2, 5, 6, 4, 3]
num.sort()
print(num)
num.sort(reverse= True)
print(num) 

num_sorted = sorted(num)
print(num_sorted)

print(min(num))
print(max(num))
print(sum(num))

# Index: Find the index of a specific item in the list
print(Courses.index('Math'))  # Outputs: 2
print(Courses.index('Art'))   # Outputs: 5

print('Math' in Courses) # Outputs: True
print('Biology' in Courses) # Outputs: False    

# looping 

# Using a for loop to iterate over a list
for course in Courses:
    print(course)

# Using a while loop to iterate over a list

i = 0
while i < len(Courses):  
    print(Courses[i])
    i += 1

# Using the enumerate function to get both the index and the item in the list
for index, course in enumerate(Courses):
    print(f"Index: {index}, Course: {course}")

for index, course in enumerate(Courses,start= 1):
    print(f"Index: {index}, Course: {course}")

# Changing a list to a string 
Names = ['Mohammed','John','Karen','Hady']
Name_str = ' - '.join(Names)

#print(Name_str)

# Splitting the string into words
new_names = Name_str.split(' - ')
print(Name_str)
print(new_names)

# tuples

# Initializing a tuple of courses

Courses_tuple = ('History', 'Math', 'Physics', 'Computer Science')

# Unpacking the tuple into variables

history, math, physics, computer_science = Courses_tuple

print(history)
print(math)
print(physics)

# A tuple does not change 
# Append: Adding an item to a tuple is not allowed

# Sets
Courses_Sets = {'History', 'Math','Physical'}

# Adding an item to a set
Courses_Sets.add('Computer Science')
print(Courses_Sets)

# Removing an item from a set

Courses_Sets.remove('Math')
print(Courses_Sets)

# Union: Get the union of two sets

set_1 = {'History', 'Math', 'Physics'}
set_2 = {'Computer Science', 'Biology', 'Math'}

union_set = set_1.union(set_2)
print(union_set)

# Intersection: Get the intersection of two sets

intersection_set = set_1.intersection(set_2)
print(intersection_set)

# Difference: Get the difference between two sets

difference_set = set_1.difference(set_2)
print(difference_set)

# Difference Update: Remove the items in the second set from the first set

set_1.difference_update(set_2)
print(set_1)

# Sets in Looping

for course in set_1:
    print(course)

# Checking if an item exists in a set

set_1 = {'History', 'Math', 'Physics'}

print('Math' in set_1) # Outputs: True
print('Biology' in set_1) # Outputs: False

# Nested Sets

nested_set = {
    'History': {'World War I', 'World War II'},
    'Math': {'Algebra', 'Calculus'},
    'Science': {'Physics', 'Chemistry'}
}

print(nested_set['Math'])

# Checking if an item exists in a nested set

print('Algebra' in nested_set['Math']) # Outputs: True
print('Biology' in nested_set['Math']) # Outputs: False

################################################################
# Empty List

empty_list = []
empty_list = list()

# Empty Tuple

empty_tuple = ()
empty_tuple = tuple()

# Empty Set

empty_set = {}
empty_set = set()

# Checking if a list is empty

print(empty_list)
print(empty_list == [])

# Same with Tuple and Sets