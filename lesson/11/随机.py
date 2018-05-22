import random
nums1 = []
nums2 = []
for _ in range(10):
    nums1.append(random.randint(10,20))
    nums2.append(random.randint(10,20))
print(nums1,nums2)

nums1 = set(nums1)
nums2 = set(nums2)

total = nums1 | nums2
norepeat = nums1 & nums2
# repeat = (nums1 - norepeat) | (nums2 - norepeat) 
repeat = nums1 ^ nums2

print(nums1)
print(nums2)
print("两组共有{}个不同的数字,分别是{}".format(len(total),total))
print("2组中，重复的数字有{}个，分别是{}".format(len(norepeat),norepeat))
print("2组中，不重复的数字有{}个，分别是{}".format(len(repeat),repeat))