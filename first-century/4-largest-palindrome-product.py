"""
Problem 4: Largest Palindrome Product

Find the largest palindrome made from the product of two 3-digit numbers.
"""

digits = 3
result = 0

def reverse_number(n):
    return int(str(n)[::-1])

for i in range(10**(digits-1),10**digits):
    for j in range(10**(digits-1),10**digits):
        prod = i * j
        if (prod == reverse_number(prod)) and (prod > result):
            result = prod
print(result)
