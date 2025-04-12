"""
Problem 3: Largest Prime Factor

What is the largest prime factor of the number 600851475143?
"""

from math import sqrt

number = 600851475143
root = sqrt(number)
i = 2

while i <= root:
    if number % i == 0:
        number = number // i
        root = sqrt(number)
        i = 1
    i += 1

print(number)

