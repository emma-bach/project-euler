"""
Problem 6: Sum Square Difference

Find the difference between the sum of the squares and
the square of the sum of the first one hundred natural numbers.
"""
# Problem assumes that 0 is not a natural number.

upper = 100

sum_squares = sum([i**2 for i in range(upper + 1)])
square_sum = sum([i for i in range(upper + 1)])**2

print(square_sum - sum_squares)
