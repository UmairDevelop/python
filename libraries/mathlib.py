import math

#Math module
print(math.pi) # Holds the value of π
print(math.e) # Holds the valure of euler's number
print(math.inf) # Represents positive infinity
print(math.nan) # Represents "Not a Number"

print(math.ceil(5.6)) # Rounds up the number
print(math.floor(5.6)) # Rounds down the number
print(math.trunc(4.7)) # Removes the decimal part
print(math.fabs(-7.5)) # Turns negative to positive

print(math.pow(2,3)) # Power function from math module
print(pow(2,3))  # Python Built-in pow function
print(math.sqrt(16)) # Square root function   
print(math.isqrt(4)) # Integer square root

print(math.log(5)) # Logarithm calculation
print(math.log10(100)) # Logarithm base 10
print(math.log2(8)) # Logarithm base 2

print(math.sin(math.radians(90))) # Sine function, input in radians
print(math.degrees(math.asin(1))) # Converts radians to degrees

print(math.comb(5,3)) # Returns the number of ways to choose k items from n items without repetition and without order
print(math.perm(5,3)) # Returns the number of ways to choose k items from n items without repetition and with order
print(math.factorial(5)) # Returns the factorial of a number
print(math.gcd(48,18)) # Returns the greatest common divisor
print(math.lcm(4,6)) # Returns the least common multiple
print(math.isclose(0.2 + 0.2, 0.4)) # Checks if two values are similar within a tolerance