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