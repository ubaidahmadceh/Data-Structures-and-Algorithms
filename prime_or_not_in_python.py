
num = 8
if num > 1:
    for i in range(2,num):
        if num%i == 0:
            print("Not a Prime")
            break
        else:
            print("Prime")
            break
