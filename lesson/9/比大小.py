nums = []
for i in range(3):
    nums.append(int(input('{}: '.format(i))))
a = nums[0] 
b = nums[1]
c = nums[2]

# 1、简单的逻辑判断
# if a >= b:
#     if a >= c:
#         if b >= c:
#             print(a,b,c)
#         else:
#             print(a,c,b)
#     else:
#         print(c,a,b)
# else:
#     if b >= c:
#         if a >= c:
#             print(b,a,c)
#         else:
#             print(b,c,a)
#     else:
#         print(c,b,a)

# 2、使用max、min函数
# while True:
#     cur = max(nums)
#     print(cur)
#     nums.remove(cur)
#     if len(nums) == 1:
#         print(nums[0])
#         break

# 3、使用sort函数
# nums.sort()
# print(nums)

