"""
Problem 10: Summation of Primes

Find the sum of all primes below two million.
"""
from math import sqrt, ceil

def sum_primes(upper: int) -> int:
    list = [True] * upper

    """
    Implementation of the sieve of Eratosthenes

    The most important realization is that we don't need to sieve
    by primes greater than sqrt(upper), since we've already detected every
    integer multiple of those primes thats smaller than upper.
    """

    for i in range(2,ceil(sqrt(upper))):
        if(list[i] == True):
            for j in range(i**2, upper, i):
                list[j] = False

    sum = 0
    for i in range(2,upper):
        if(list[i] == True):
            sum += i

    return sum


if __name__ == "__main__":
    print(sum_primes(2000000))
