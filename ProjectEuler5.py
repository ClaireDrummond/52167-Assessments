# Claire Drummond 2018-02-20
# Project Euler Problem No. 5

#2520 is the smallest number that can be divided by each of numbers 1-10 without remainder
# ref: https://projecteuler.net/

for i in range (1, 11):
    print (2520 / i)
    
# above statment correct

# smallest number that is divisible by (1,21)
def isdivisible1to20(n):
    for i in range (1,21):
        if n % i != 0:
            return False
    return True       

# starting at number 1, is it divisible by 1-20
n = 1

while True:
    if isdivisible1to20(n):
        break
    n = n + 1
 # keep adding 1 to the number until the number is divisible by all numbers 1-20

print(n)

#program takes a bit too long to run.  Must revisit