def factorial(n):
    total = 1
    for i in range(n):
        total *= (i+1)
    return total
print(factorial(5))
