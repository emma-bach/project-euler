"""
Problem 9: Special Pythagorean Triplet

Find the product abc such that a**2 + b**2 = c**2 and a+b+c = 1000
"""
def generate_triplet(sum: int):
    for k in range(1, sum):
        for n in range(1, sum):
            for m in range(1, sum):
                # Formula for generating pythagorean triples taken from wikipedia
                a = k * (m**2 - n**2)
                b = k * (2 * m * n)
                c = k * (m**2 + n**2)
                if(a + b + c == 1000):
                    return a*b*c
    return -1

if __name__ == "__main__":
    print(generate_triplet(1000))
