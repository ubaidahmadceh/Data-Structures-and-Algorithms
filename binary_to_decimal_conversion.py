# Raw approach

import numpy as np
binary_number=101
binary_number_str = str(binary_number)
binary_number_list = []
for i in binary_number_str:
    binary_number_list.append(int(i))
binary_number_list_rev = []
for i in range(1, len(binary_number_list)+1):
    binary_number_list_rev.append(binary_number_list[-i])
powers_of_2 = []
for i in range(len(binary_number_list)):
    powers_of_2.append(2**i)
decimal_number = np.dot(np.array(binary_number_list_rev), np.array(powers_of_2))
print(decimal_number)


# 






