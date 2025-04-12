"""
Problem 9: Special Pythagorean Triplet

Find the product abc such that a**2 + b**2 = c**2 and a+b+c = 1000
"""
from math import prod

def generate_triplet(target: int):
    for k in range(1, target // 3):
        for m in range(1, target // k):
            for n in range(1, min(m, target // (k * m))):
                """ 
                The loop bounds are sufficient because we have m > n and a,b,c < target
                
                I use a formula for generating pythagorean triples taken from Wikipedia.
               
                My implementation generates some triples twice. 
                To avoid this, we'd need to ensure m and n are coprime,
                which seems to slow to be worth it.

                We can deduce from this that the set of all possible
                perimeters a+b+c of pythagorean triangles is generated by:
                a+b+c = k * 2m(m + n) with m > n
                """
                a = k * (m**2 - n**2)
                b = k * (2 * m * n)
                c = k * (m**2 + n**2)
                if(a + b + c == target):
                    return (a,b,c)
    return (0,0,0)

def generate_all_triplets(target):
    for i in range(target + 1):
        triplet = generate_triplet(i)
        if triplet[0] != 0:
            print(f"{sum(triplet)} = {triplet[0]} + {triplet[1]} + {triplet[2]}")

if __name__ == "__main__":
    print(prod(generate_triplet(1000)))
