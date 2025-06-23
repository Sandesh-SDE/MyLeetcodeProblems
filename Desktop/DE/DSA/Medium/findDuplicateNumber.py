'''
287. Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

 

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [3,3,3,3,3]
Output: 3

'''

# using set
def findDuplicateNumber1(nums):
    my_set = set()
    
    for i in nums:
        if i in my_set:
            return i
        else:
            my_set.add(i)

# using dict
def findDuplicateNumber(nums):
    my_dict = {}
    
    for i in nums:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1

    for i,j in my_dict.items():
        if j > 1:
            return i
            
    

nums1 = [1,3,4,2,2]
nums2 = [3,1,3,4,2]
nums3 = [3,3,3,3,3]

op1 = findDuplicateNumber(nums1)
op2 = findDuplicateNumber(nums2)
op3 = findDuplicateNumber(nums3)

print(op1, op2, op3)

'''
| Approach      | Time Complexity | Space Complexity | Returns on first dup | Notes                               |
| ------------- | --------------- | ---------------- | -------------------- | ----------------------------------- |
| Set           | O(n)            | O(n)             | ✅                    | Simple and fast                     |
| Dictionary    | O(n)            | O(n)             | ✅                    | Slightly more overhead than set     |
| Floyd’s Cycle | O(n)            | O(1)             | ✅                    | Best for constraints-based problems |

'''