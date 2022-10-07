def factorial(n):
    fact = 1
    for i in range(n):
        fact *= n-i
    return fact

def ncr(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))

for i in range(5):
    for j in range(i+1):
        print(int(ncr(i,j))," ", end="")
    print("")