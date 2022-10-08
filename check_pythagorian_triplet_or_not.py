x=3
y=4
z=5

value_list = [x,y,z]

a=max(value_list)
value_list.remove(a)

sum_sqr_b = value_list[0]**2
sum_sqr_c = value_list[1]**2

if a**2 == sum_sqr_b + sum_sqr_c:
    print("It's a pythagorian Triplet")
else:
    print("It's NOT a pythagorian Triplet")
