# Hi There, Hope you are doing well. I help students with their coursework and projects. I have handled many subjects for students from universities like CalU, Morgan State, SRU etc. WhatsApp: +923484122900 , Email: ubaidp1049@gmail.com 
#Thanks
# ----------------------------------------------------------------------------

# Reverse a number by remainder-modulus(%) approach 

n = 7547
n = str(n)
store = []

for i in n:
    store.append(int(i)%int(n))

store_reversed = []
for i in range(1, len(store)+1):
    store_reversed.append(store[-i])

num_reversed_str = ""
for i in store_reversed:
    num_reversed_str += str(i)

print(int(num_reversed_str))