# Define a string variable
message = "Hello World"

# Print the variable
print(message)

# Print the length of the variable (number of characters in the string)
print(len(message))

# String slicing
# Print characters from the start up to, but not including, index 5
print(message[:5]) 

# Print characters from index 6 to the end
print(message[6:]) 

#For more information on slicing : https://www.youtube.com/watch?v=ajrtAuDg3yw&t=0s

# Methods: Functions that belong to string objects
# Convert the string to all lowercase letters
print(message.lower())

# Convert the string to all uppercase letters
print(message.upper())

# Count the occurrences of the substring 'll' in the string
print(message.count('ll'))

# Find the starting index of the substring 'World'
print(message.find('World'))

# Find the starting index of the substring 'Universe' (returns -1 if not found)
print(message.find("Universe")) 

# Replace the substring 'World' with 'Universe' and return a new string
new_message = message.replace('World', 'Universe') 
print(new_message)

# Concatenate strings using the plus operator
greeting = 'Hello'
name = 'Michael'
message = greeting + ', ' + name + ' Welcome' 
print(message)

# String formatting using .format()
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

# String formatting using f-strings (introduced in Python 3.6, more readable)
message = f'{greeting}, {name}. Welcome!' 
print(message)

# For more information on string formatting : https://www.youtube.com/watch?v=vTX3IwquFkc&t=0s

# Additional resources:
# To see all available methods for a string object, uncomment the line below:
# print(dir(name))

# To get detailed help on a specific method, e.g., str.lower(), uncomment the line below:
# print(help(str.lower))
