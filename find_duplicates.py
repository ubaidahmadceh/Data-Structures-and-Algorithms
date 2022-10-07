# def check_duplicates(nums):
#     for i in nums:
#         if nums.count(i) > 1:
#             return True
#         else:
#             return False

def check_duplicates(nums):
    for i in nums:
        if nums.count(i) > 1:
            print(True)
            break
        

check_duplicates([2,14,18,22,22])
# print(check_duplicates([2,14,18,22,22]))

# print([2,14,18,22,22].count(22))

        
        