# Iterative Approach
def factorial(n):
    fact = 1
    for i in range(n):
        fact *= n-i
    return fact

print(factorial(4))