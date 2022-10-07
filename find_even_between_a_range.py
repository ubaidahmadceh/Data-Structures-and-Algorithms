# evens = []
# for num in range(1, 11):
#     if num%2==0:
#         evens.append(num)

# print(evens)


primes = []

for num in range(1, 11):
    flag = 0
    for i in range(2,num):
        if num%i==0:
            flag=0
        else:
            flag=1
    if flag==1:
        primes.append(num)
print(set(primes))

