'''
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

'''

'''

✅ Rule: A number num is a start if num - 1 is not in the set

🚀 Preview: Optimized Approach (HashSet)
If you use a HashSet, you can:

Look up elements in O(1) time

Only start a sequence if num - 1 is not in the set (i.e., it’s the start)

Avoid redundant work

➡ This gives you O(n) time.

----------------------------------------------------------------

Step 1: Add all numbers to a set
This allows fast O(1) lookups to check if a number exists.

It also automatically removes duplicates.

Step 2: Loop through each number in the set
For each number, check:

Is it the start of a sequence?

That means: num - 1 is NOT in the set

If it is the start, then:

Count how long the sequence continues:

While num + 1, num + 2, … are in the set

Keep incrementing a counter

Step 3: Track the maximum sequence length
'''

def longestConsecutive(nums):

    my_set = set(nums)
    print(my_set)

    length = 0 


    for n in nums:

        if n-1 not in my_set:

            # if n - 1 not in set then its a starting sequence

            current = n
            curr_length = 1

            while current+1 in my_set:
                current += 1
                curr_length += 1

            length = max(length, curr_length)

    print(length)




# nums = [100,4,200,1,3,2]
# nums = [0,3,7,2,5,8,4,6,0,1]
nums = [1,0,1,2]
# nums = [9,1,4,7,3,-1,0,5,8,-1,6]
longestConsecutive(nums)