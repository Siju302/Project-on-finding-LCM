import math

# Get two numbers from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Calculate LCM using GCD
lcm = abs(a * b) // math.gcd(a, b)

print(f"The LCM of {a} and {b} is {lcm}")
