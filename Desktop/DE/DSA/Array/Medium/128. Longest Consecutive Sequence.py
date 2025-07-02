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


'''
Step by Step Algorithm
Convert List to Set:

num_set = set(nums)
Convert the list nums to a set num_set to allow O(1) time complexity for checking the presence of elements. This step ensures that we can quickly determine if a number is part of the sequence.
Initialize the Longest Sequence Length:

longest = 0
Initialize a variable longest to keep track of the length of the longest consecutive sequence found so far. Set it to 0 initially.
Iterate Through Each Number in the List:

for n in nums:
Iterate through each number n in the list nums.
Check if Current Number is the Start of a Sequence:

if n - 1 not in num_set:
For each number n, check if n - 1 is not in num_set. This check determines if n is the start of a new sequence. If n - 1 is not present, it means n is the smallest number in the current sequence.
Initialize Length of Current Sequence:

length = 1
If n is the start of a new sequence, initialize a variable length to 1. This variable will keep track of the length of the current sequence starting with n.
Extend the Current Sequence:

while n + length in num_set:
    length += 1
Use a while loop to extend the current sequence. While n + length is present in num_set, increment length. This loop continues until the next consecutive number is not found in the set, indicating the end of the current sequence.
Update the Longest Sequence Length:

longest = max(longest, length)
After determining the length of the current sequence, update longest by taking the maximum of longest and length. This ensures that longest always holds the length of the longest consecutive sequence found so far.
Return the Result:

return longest
After iterating through all numbers in the list, return longest, which now holds the length of the longest consecutive sequence.
'''