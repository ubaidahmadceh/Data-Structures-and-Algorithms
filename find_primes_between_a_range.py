# Hi There, Hope you are doing well. I help students with their coursework, Homework, Assignments and projects. I have handled many subjects for students from universities like CalU, Morgan State, SRU etc. WhatsApp: +923484122900 , Email: ubaidp1049@gmail.com 
#Thanks
# ----------------------------------------------------------------------------

range_start= int(input("Enter range_start: "))
range_end = int(input("Enter range_end: "))

primes = []
for num in range(range_start, range_end+1):
    if num > 1:
        for i in range(2,num):
            if num%i==0:
                primes.append(i)


print(set(primes))