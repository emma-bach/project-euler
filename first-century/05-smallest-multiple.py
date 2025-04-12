"""
Problem 5: Smallest Multiple

What is the smallest number that is divisible without remainder
by all the numbers from 1 to 20?
"""

upper = 20
prod = 2

# Euclidean Algorithm for finding the greatest common divisor
def gcd(i, j):
    while j != 0:
        i, j = j, i % j
    return i

for i in range(3, upper + 1):
    if prod % i != 0:
        prod *= i // gcd(prod,i)
print(prod)
