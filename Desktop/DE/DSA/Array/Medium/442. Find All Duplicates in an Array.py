'''
442. Find All Duplicates in an Array

Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:
Input: nums = [1,1,2]
Output: [1]

Example 3:
Input: nums = [1]
Output: []

'''

# Using Brute force we can have O(N2) Time complexity
def findAllDuplicatefromArray1(nums):

    duplicate_numbers = []

    for i in range(len(nums)):
        j = 0
        while j < i:

            if nums[j] == nums[i]:
                duplicate_numbers.append(nums[j])                
            
            j += 1

    print(duplicate_numbers)

# Using Set we can have O(N) time complexity
def findAllDuplicatefromArray(nums):

    duplicate_numbers = []
    my_set = set()

    for i in nums:
        if i in my_set:
            duplicate_numbers.append(i)
        else:
            my_set.add(i)

    print(duplicate_numbers, my_set)

    


nums1 = [4,3,2,7,8,2,3,1]
nums2 = [1,1,2]
nums3 = [1]
op = findAllDuplicatefromArray(nums1)
op = findAllDuplicatefromArray(nums2)
op = findAllDuplicatefromArray(nums3)