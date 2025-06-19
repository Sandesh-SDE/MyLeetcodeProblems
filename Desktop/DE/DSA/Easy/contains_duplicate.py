'''
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false

Explanation:
All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

'''


#  O(N) - Linear Running time complexity
def containsDuplicate1(nums):

    seen = {}

    for i, v in enumerate(nums):

        if v in seen:
            return True
        
        seen[v] = i

    return False

def containsDuplicate2(nums):

    seen = set()

    for i, v in enumerate(nums):

        if v in seen:
            return True
        
        seen.add(v)

    return False

def containsDuplicate(nums):
    return not len(nums) == len(set(nums))





nums1 = [1,2,3,1]
nums2 = [1,2,3,4]
nums3 = [1,1,1,3,3,4,3,2,4,2]
op1 = containsDuplicate(nums1)
op2 = containsDuplicate(nums2)
op3 = containsDuplicate(nums3)

print(op1, op2, op3)


'''
| Approach                 | Time       | Space | Best Use Case                             |
| ------------------------ | ---------- | ----- | ----------------------------------------- |
| Brute Force              | O(n²)      | O(1)  | Very small inputs, no extra space allowed |
| HashSet (Optimal)        | O(n)       | O(n)  | General purpose, best for performance     |
| `len(set(nums))`         | O(n)       | O(n)  | Concise Python code                       |

'''
