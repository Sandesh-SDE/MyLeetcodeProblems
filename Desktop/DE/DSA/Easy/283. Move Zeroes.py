'''
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

'''

# 74 / 75 testcases passed
# Brute force with O(N2)

def moveZeros(nums):

    n = 0
    for i in range(len(nums)):
        print(i, n)
        if nums[i] != 0:
            nums[n], nums[i] = nums[i], nums[n]
            n += 1
            
    print(nums)

def moveZeros1(nums):
    if len(nums) == 1:
        return nums
    
    for i in range(len(nums)):

        j = 0
        while j < i:
            # print(j, i, nums[j], nums[i])

            if nums[j] == 0:
                nums[j], nums[i] = nums[i], nums[j]

            j += 1

    print(nums)
    return nums

nums1 = [0,1,0,3,12]
nums2 = [0]
nums3 = [0,1,0,3,12, 0, 7, 0, 0, 3,2,1]




op1 = moveZeros(nums1)
# op2 = moveZeros(nums2)
# op2 = moveZeros(nums3)