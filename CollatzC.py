# Claire Drummond 2018-02-11

# Collatz Conjecture

# ref: https://en.wikipedia.org/wiki/Collatz_conjecture

n = int(input("Please enter an integer: "))

while n !=1:
    if n % 2 == 0:
        n = n/2
        print (n)
    else:
        n = (n * 3) + 1 
        print (n)   


# If the previous integer is even, the next integer is divided by 2
# However if the previous integer is odd, the next integer is 3 times the previous integer plus 1
# The conjecture is that no matter what value of n, the sequence will always reach 1
