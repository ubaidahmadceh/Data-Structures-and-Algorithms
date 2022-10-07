# Hi There, Hope you are doing well. I help students with their coursework and projects. I have handled many subjects for students from universities like CalU, Morgan State, SRU etc. WhatsApp: +923484122900 , Email: ubaidp1049@gmail.com 
#Thanks
# ----------------------------------------------------------------------------

# Iterative Approach

# n = 5
# fact = 1
# for i in range(n):
#     fact *= n-i
# print(fact)

# ------------------------------------------------------
# Recursive Approach

# def fact_calc(n):
#     if n == 1:
#         return n
#     else:
#         return fact_calc(n-1)*n
# print(fact_calc(1))

def fact_calc(n):
    if n > 1:
        return n*fact_calc(n-1)
    else:
        return 1
        
print(fact_calc(5))