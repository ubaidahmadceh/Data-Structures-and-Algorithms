def factorial(n):
    fact = 1
    for i in range(n):
        fact *= n-i
    return fact

# formula for binary coefficient (nCr) = n!/(n-r)!*r!
n=5
r=2

ncr=factorial(n)/(factorial(r)*factorial(n-r))
print(ncr)