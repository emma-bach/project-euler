# Problem 2: Even Fibonacci numbers
# By considering the terms in the fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

sum = 0
upper = 4000000

fib1 = 1
fib2 = 2

while(fib2 <= upper):
    if fib2 % 2 == 0:
        sum += fib2
    temp = fib2
    fib2 = fib1 + fib2
    fib1 = temp

print(sum)

