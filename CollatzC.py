# Claire Drummond 2018-02-11

# Collatz Conjecture

# ref: https://en.wikipedia.org/wiki/Collatz_conjecture

n = int(input("Please enter an integer: ")) #This allows me to input any integer at the command prompt

while n !=1: # while n is not equal to 1
    if n % 2 == 0: # if there is no remainder when you divide n by 2
        n = n/2 # divide n by 2
        print (n) # print n
    else: # otherwise
        n = (n * 3) + 1 # multiply n by 3 and add 1
        print (n)   # print n


# If the previous integer is even, the next integer is divided by 2
# However if the previous integer is odd, the next integer is 3 times the previous integer plus 1
# The conjecture is that no matter what value of n, the sequence will always reach 1
