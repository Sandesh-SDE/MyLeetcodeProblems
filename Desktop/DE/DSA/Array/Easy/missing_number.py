'''
268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.


Example 1:
Input: nums = [3,0,1]
Output: 2

Explanation:
n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2

Explanation:
n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8

Explanation:
n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

'''

# brute force O(N)
'''
my brute force approch is 

step 1 : first move len(nums) to new_list 
step 2 : then deduct 1 from last index of new_list
step 3 : append deducted value to new_list again
step 4 : apply a for loop for new_list and check value is present in nums
step 5 : if not present return it

'''
def missing_number(nums):

    new_list = []

    new_list.append(len(nums))

    for _ in range(len(nums)):
        v = new_list[-1] - 1
        new_list.append(v)

    for i in new_list:
        if i not in nums:
            return i
        
def missing_number2(nums):

    n = len(nums)

    expected_sum = n * (n + 1) // 2
    total_sum = sum(nums)

    return expected_sum - total_sum
        

nums1 = [3,0,1]
nums2 = [0,1]
nums3 = [9,6,4,2,3,5,7,0,1]
op1 = missing_number(nums1)
op2 = missing_number(nums2)
op3 = missing_number(nums3)
print(op1, op2, op3)


'''

| Approach              | Time Complexity | Space Complexity | Remarks                    |
| --------------------- | --------------- | ---------------- | -------------------------- |
| Your current approach | O(n²)           | O(n)             | Works but inefficient      |
| Sum formula method    | O(n)            | O(1)             | Best for clarity and speed |


'''
