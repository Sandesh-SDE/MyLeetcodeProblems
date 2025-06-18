'''
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

'''

'''

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

'''


'''

| Method              | Time       | Space | Returns        | Notes                        |
| ------------------- | ---------- | ----- | -------------- | ---------------------------- |
| Brute Force         | O(n²)      | O(1)  | Indices        | Simple but inefficient       |
| Hash Map            | O(n)       | O(n)  | Indices        | Best for unsorted input      |
| Set Check Only      | O(n)       | O(n)  | True/False     | Use for existence check only |

'''

# O(N2)
# Brute Force	O(n²)	O(1)	Indices	Simple but inefficient
def twoSum1(nums, target):

    index = []

    for i in range(len(nums)):
        j = 0
        while j < i:
            
            if nums[i] + nums[j] == target:
                index.append(j)
                index.append(i)
                
                
            j += 1

    return index

# Hash Map	O(n)	O(n)	Indices	Best for unsorted input
def twoSum3(nums, target):

    seen = {}
    for i, v in enumerate(nums):
        c = target - v
        # print(f"{target} - {v} = {c} , {i}")

        if c in seen:
            # print(seen[c], i)
            return seen[c], i

        seen[v] = i



# Set Check Only	O(n)	O(n)	True/False	Use for existence check only
def twoSum2(nums, target):

    seen = set()

    for i in nums:
        if target-i in seen:
            return True

        seen.add(i)

        
        


nums1 = [3,2,4]
target1 = 6

nums2 = [2,7,11,15]
target2 = 9

nums3 = [3,3]
target3 = 6

# op = twoSum1(nums, target)
# print(op)

op1 = twoSum1(nums2, target2)
print(op1)

# op2 = twoSum2(nums2, target2)
# print(op2)

# op3 = twoSum2(nums3, target3)
# print(op3)

