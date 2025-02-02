def square_number(nums):
    for i in nums:
        yield (i*i)

my_num=square_number([1,2,3,4,5])
# print(type(my_num))
# print(next(my_num))
# print(next(my_num))
for i in my_num:
    print(i)
