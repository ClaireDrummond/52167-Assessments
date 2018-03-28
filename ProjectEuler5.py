# Claire Drummond 2018-02-20
# Project Euler Problem No. 5

#2520 is the smallest number that can be divided by each of numbers 1-10 without remainder
# ref: https://projecteuler.net/

for i in range (1, 11):
    print (2520 / i)
    
# above statement correct

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



# Alternative Solution to Project Euler 5
# Ref: https://github.com/nayuki/Project-Euler-solutions/blob/master/python/p005.py


import fractions





# The smallest number n that is evenly divisible by every number in a set {k1, k2, ..., k_m}

# is also known as the lowest common multiple (LCM) of the set of numbers.

# The LCM of two natural numbers x and y is given by LCM(x, y) = x * y / GCD(x, y).

# When LCM is applied to a collection of numbers, it is commutative, associative, and idempotent.

# Hence LCM(k1, k2, ..., k_m) = LCM(...(LCM(LCM(k1, k2), k3)...), k_m).

def compute():

	ans = 1

	for i in range(1, 21):

		ans *= i // fractions.gcd(i, ans)

	return str(ans)





if __name__ == "__main__":

	print(compute())

 #Very efficient code.    