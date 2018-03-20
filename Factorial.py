# Claire Drummond 2018-03-20
# Factorial Numbers Exercise 6

def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num
print("The factorial of number 5 is:",factorial(5))
print("The factorial of number 7 is:",factorial(7))
print("The factorial of number 10 is:",factorial(10))

# Alternative Solution
# ref: https://stackoverflow.com/questions/5136447/function-for-factorial-in-python
from math import factorial
print("The factorial of number 5 is:",factorial(5))
print("The factorial of number 7 is:",factorial(7))
print("The factorial of number 10 is:",factorial(10)) 