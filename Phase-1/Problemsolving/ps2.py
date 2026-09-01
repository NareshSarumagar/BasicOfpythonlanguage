# Find the Largest Number (without max())
# Given nums = [23, 67, 12, 89, 45] , find the biggest number without using
# max() .
# Uses: loop · if · comparison · "best so far" pattern


nums = [23,67,12,89,45]
num = nums[0]

for i in nums:
    if num<i:
        num = i
print(num)