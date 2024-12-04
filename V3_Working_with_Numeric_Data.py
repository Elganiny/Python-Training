# Arithmetic Operations in Python with Examples

# Addition: Add two numbers
x = 10
y = 5
print("Addition:", x + y)  # Output: 15

# Subtraction: Subtract the second number from the first
print("Subtraction:", x - y)  # Output: 5

# Multiplication: Multiply two numbers
print("Multiplication:", x * y)  # Output: 50

# Division: Divide the first number by the second (returns a float)
print("Division:", x / y)  # Output: 2.0

# Floor Division: Divide and round down to the nearest whole number
print("Floor Division:", x // y)  # Output: 2

# Exponentiation: Raise the first number to the power of the second
print("Exponentiation:", x ** y)  # Output: 100000 (10 raised to the power of 5)

# Modulus: Return the remainder when the first number is divided by the second
print("Modulus:", x % y)  # Output: 0 (10 is evenly divisible by 5)

# Increment Operations
num = 1
num = num + 1  # Increment using addition
num += 1       # Increment using shorthand
print("Incremented Value:", num)  # Output: 3

# Absolute Value: Returns the absolute (positive) value of a number
print("Absolute Value:", abs(-3))  # Output: 3

# Rounding: Round a number to the nearest integer or specified decimal places
print("Round to nearest integer:", round(3.761))        # Output: 4
print("Round to 1 decimal place:", round(3.761, 1))     # Output: 3.8
print("Round to 2 decimal places:", round(3.761, 2))    # Output: 3.76

# Comparisons
# Comparing two numbers and returning Boolean values (True/False)
print("Equal:", x == y)         # False
print("Not Equal:", x != y)     # True
print("Greater Than:", x > y)   # True
print("Less Than:", x < y)      # False
print("Greater or Equal:", x >= y)  # True
print("Less or Equal:", x <= y)     # False

# Casting: Converting string numbers to integers for mathematical operations
num_1 = '100'
num_2 = '200'

# Convert string to integer
num_1 = int(num_1)
num_2 = int(num_2)

# Perform addition after casting
print("Sum after casting:", num_1 + num_2)  # Output: 300
