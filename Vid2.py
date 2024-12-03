#HEllo world variable 
message = "Hello World"

print(message)
#Prints the length of the variable
print(len(message))
#This is called "slicing"
#It does not print the value of index 5
print(message[:5]) 
print(message[6:]) 
#For more information on slicing : https://www.youtube.com/watch?v=ajrtAuDg3yw&t=0s

#Methodes : functions but belongs to an objects
print(message.lower())      # All letters are small 
print(message.upper())      # All letters are Capital
print(message.count('ll'))  # Find the count of a specific part
print(message.find('World'))# Find the start index of any text (if there is more than one it will return the index of the first one)
print(message.find("Universe")) # Not found = -1

new_message = 