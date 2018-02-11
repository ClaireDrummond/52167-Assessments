# Claire Drummond W1 and W2 Exercises

# Week 1 Exercise

# A program that displays Fibonacci numbers.



def fib(n):

  """This function returns the nth Fibonacci number."""

  i = 0

  j = 1

  n = n - 1



  while n >= 0:

    i, j = j, i + j

    n = n - 1

  

  return i



# Test the function with the following value.

x = 8

ans = fib(x)

print("Fibonacci number", x, "is", ans)


# My name is Claire, so the first and last letter of my name (C + E = 3 + 5), give the number 8. The 8th Fibonacci number is 21



# Week 2 Exercise

# A program that displays Fibonacci numbers using people's names.



def fib(n):

  """This function returns the nth Fibonacci number."""

  i = 0

  j = 1

  n = n - 1



  while n >= 0:

    i, j = j, i + j

    n = n - 1

  

  return i



name = "Drummond"

first = name[0]

last = name[-1]

firstno = ord(first)

lastno = ord(last)

x = firstno + lastno



ans = fib(x)

print("My surname is", name)

print("The first letter", first, "is number", firstno)

print("The last letter", last, "is number", lastno)

print("Fibonacci number", x, "is", ans)

# The ord() and chr() are exactly the opposite/reverse functions of each other.
# We know that computer understands only bits and bytes. The characters we type in or feed into it are really encoded as bits. For us humans, we interpret these bits as some numbers that represent those characters we fed. These are what we can say ASCII codes.
# Like
# ASCII code for ‘A’ is 65, ‘a’ is 97, etc.
# ord()
# It gives the ASCII code of the character.
# Eg: ord(‘a’) is 97
# chr()
# It gives the corresponding character for given ASCII code.
# Eg: chr(97) is ‘a’
