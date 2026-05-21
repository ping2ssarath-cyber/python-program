numbers = []

# Get two numbers from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Add numbers to list
numbers.append(num1)
numbers.append(num2)

# Add using list
total = sum(numbers) // total = number[0]+number[1]

# Display
print("Numbers in list:", numbers)
print("Sum of two numbers is:", total)
