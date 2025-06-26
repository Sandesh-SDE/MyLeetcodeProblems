'''
448. Find All Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
Input: nums = [1,1]
Output: [2]

'''

# Accepted 28 test cases out of 35
'''
step 1: remove all duplicates from nums
step 2: append 0 at end after removing those duplicates if 2 then 2 0s if 3 then 3 0s
step 3: loop from 1st index and compare index of 0 + value 1  is not equal to next value then 
step 4: get the index and get the value of 0 + value 1 and instert to that index and also append it to new array
step 5: pop the last item that is 0

step 6: return the missing_number list
'''

def findAllDisappearedNumber1(nums):

    missing_number = []

    removed_duplicate_list = list(set(nums))

    for _ in range(len(nums) - len(removed_duplicate_list)):
        removed_duplicate_list.append(0)

    print(removed_duplicate_list)

    j = 0
    for i in range(1, len(removed_duplicate_list)):
        if removed_duplicate_list[j] + 1 != removed_duplicate_list[i]:
            # print(True, removed_duplicate_list[j] ,"+", 1 ,"!=", removed_duplicate_list[i],"index==", i)

            removed_duplicate_list.insert(i, removed_duplicate_list[j] + 1)
            missing_number.append(removed_duplicate_list[j] + 1)
            removed_duplicate_list.pop()
        
        j += 1
    print(missing_number)


# method 1
def findAllDisappearedNumber(nums):

    n = len(nums)
    nums = set(nums)

    # print(n, nums)
    missing_numbers = []

    for i in range(1, n+1):
        print(i)

        if i not in nums:
            missing_numbers.append(i)

    return missing_numbers


nums1 = [4,3,2,7,8,2,3,1]
nums2 = [1,1]
# nums3 = [4,3,2,7,8,2,3,1]

op1 = findAllDisappearedNumber(nums1)
print()
# op1 = findAllDisappearedNumber(nums2)
# print()
# op1 = findAllDisappearedNumber(nums3)
