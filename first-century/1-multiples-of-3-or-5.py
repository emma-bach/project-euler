# Problem 1: Multiples of 3 or 5
# Find the sum of all multiples of 3 or 5 below 1000


def linear_time(upper,num1,num2):
    """
    Simply loop up to the upper bound and add
    a number if it is a multiple of num1 or num2.
    """
    sum = 0
    for i in range(upper):
        if i % num1 == 0 or i % num2 == 0:
            sum += i
    return sum

def constant_time(upper,num1,num2):
    """
    Let q = upper // n.
    Then the sum of the multiples of n up to upper is given by
    n * (1+2+....+q) = n * (q^2 + q)//2.

    We can get our result by adding the sum of multiples of num1
    and the sum of multiples of num2 and subtracting the sum of
    multiples of num1 * num2.
    """

    def sum_multiples(upper,n):
        q = (upper - 1) // n #We need to subtract 1 from upper since 1000 itself is excluded.
        sum = n * (q**2 + q) // 2
        print(f"Sum of multiples of {n} up to {upper}: {sum}")
        return sum

    return sum_multiples(upper,num1) + sum_multiples(upper,num2) - sum_multiples(upper,num1*num2)

if __name__ == "__main__":
    print(constant_time(1000,3,5))
