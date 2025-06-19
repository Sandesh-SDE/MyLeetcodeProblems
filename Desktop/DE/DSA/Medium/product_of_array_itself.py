'''
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:
Input: nums = [1,2,3,4] 
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

'''

def product_of_array_iteself1(nums):

    n = len(nums)
    output = [1] * n

    left = 1
    for i in range(len(nums)):
        output[i] = left
        left *= nums[i]

    right = 1
    for i in range(len(nums)-1, -1, -1):
        output[i] *= right
        right *= nums[i]

    return output

# O(N2) brute force
def product_of_array_iteself2(nums):

    mv_list = []
    op = []

    for i, v in enumerate(nums):

        nums.pop(i)
        mv_list.append(v)

        o = 1
        for j in nums:
            o *= j
        
        op.append(o)

        nums.insert(i, v)
        mv_list = []


    return op


nums1 = [1,2,3,4] 
nums2 = [-1,1,0,-3,3]
op1 = product_of_array_iteself1(nums1)
op2 = product_of_array_iteself1(nums2)

op3 = product_of_array_iteself2(nums1)
op4 = product_of_array_iteself2(nums2)

print(op1, op2)
print(op3, op4)