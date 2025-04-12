"""
Problem 7: 10 001st Prime

What is the 10 001st prime number?
"""

def brute_force(upper: int) -> int:
    counter = 1
    candidate = 3
    primes = [2]
    while(counter < upper):
        is_prime = True
        for i in primes:
            if candidate % i == 0:
                is_prime = False
        if(is_prime):
            counter += 1:
            primes += [candidate]
        candidate += 2 #No need to check even numbers
    return primes[-1]

if __name__ == "__main__":
    print(brute_force(10001))
