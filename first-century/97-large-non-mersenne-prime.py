"""
Problem 97: Large Non-Mersenne Prime

Find the last ten digits of the prime 28433 * 2**7830457 + 1
"""

digits = 10
factor = 28433
exponent = 7830457

def brute_force(digits, factor,exponent):
    result = 1
    for i in range(exponent):
        result = result * 2 % 10**digits
    return ((result * factor) + 1) % 10**digits

def iterative_squaring(digits, exponent:int):
    """
    Use the fact that e.g. 2^1001 = (2^500)^2 * 2 
    to solve the problem in time O(log(exponent))
    """
    if exponent == 1:
        return 2 
    return (iterative_squaring(digits, exponent // 2)**2 * 2**(exponent % 2)) % 10**digits

def get_cycle(digits:int, exponent:int):
    """
    Related Group Theory Problem (I don't think that this is useful for creating a general algorithm but it's very cool to think about):

    If we keep doubling and taking the modulo, we will eventually arrive at a cycle.
    We could in theory use this to calculate very large exponents, because this lets us take the exponent
    modulo the cycle length and calculate that instead.
    """
    result = 1
    counter = 1
    result_list = []
    while(True):
        result = (result * 2) % 10**digits
        for i in range(len(result_list)):
                if result_list[i] == result:
                    cycle_start = i
                    result_list = result_list[i:]
                    cycle_length = len(result_list)
                    return result_list[(exponent - cycle_start - 1) % cycle_length]
        result_list += [result]
        counter += 1



if __name__ == "__main__":
    print((factor * iterative_squaring(digits,exponent) + 1) % 10**digits)

