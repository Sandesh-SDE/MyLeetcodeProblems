'''
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.


Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

'''

def findSingleNumber(nums):

    my_dict = {}
    for i in nums:
        my_dict[i] = my_dict.get(i, 0) + 1

    for k in my_dict:
        if my_dict[k] == 1:
            print(k)
            return k

    # print(my_dict)
        
'''
| Property            | Value                                                             |
| ------------------- | ----------------------------------------------------------------- |
| 🧠 Logic            | Add/remove from set to cancel out                                 |
| ⏱ Time Complexity   | **O(n)**                                                          |
| 🧠 Space Complexity | **O(n)**                                                          |
| 🧰 Extra Space Used | Yes (`set`)                                                       |
| 🧾 Loop Count       | 1 loop                                                            |
| ✅ When to Use       | When **each number appears exactly twice** except one             |
| ⚠️ Limitations      | Fails if more than one unique or a number appears more than twice |

'''
    

# O(N) but not space efficient
def findSingleNumber2(nums):
    
    my_set = set()
    for i in nums:
        if i in my_set:
            my_set.remove(i)
        else:
            my_set.add(i)

    print(my_set)

# Time C - O(N)  Space C - O(N)
def findSingleNumber1(nums):
    result = 0
    
    for i in nums:
        result ^=  i

    print(result)

'''
| Property            | Value                                        |
| ------------------- | -------------------------------------------- |
| 🧠 Logic            | XOR cancels out duplicates                   |
| ⏱ Time Complexity   | **O(n)**                                     |
| 🧠 Space Complexity | **O(1)**                                     |
| 🧰 Extra Space Used | No                                           |
| 🧾 Loop Count       | 1 loop                                       |
| ✅ When to Use       | When **all numbers appear twice** except one |
| ⚠️ Limitations      | Fails if numbers appear more than twice      |
'''




nums1 = [2,2,1]
nums2 = [4,1,2,1,2]
nums3 = [1]

op1 = findSingleNumber(nums1)
op2 = findSingleNumber(nums2)
op3 = findSingleNumber(nums3)

# print(op1)

'''
| Approach   | Time | Space | Extra Space | Loop Count | Handles >2 Repeats | Fastest |
| ---------- | ---- | ----- | ----------- | ---------- | ------------------ | ------- |
| XOR        | O(n) | O(1)  | ❌ No        | ✅ 1        | ❌ No               | ✅ Yes   |
| Dictionary | O(n) | O(n)  | ✅ Yes       | ✅ 2        | ✅ Yes              | ⚠️ No   |
| Set Trick  | O(n) | O(n)  | ✅ Yes       | ✅ 1        | ❌ No               | ✅ Yes   |


XOR Key Properties

| Expression                             | Result | Meaning                           |
| -------------------------------------- | ------ | --------------------------------- |
| `a ^ a`                                | `0`    | A number XOR with itself is zero  |
| `a ^ 0`                                | `a`    | A number XOR with 0 is the number |
| XOR is **commutative and associative** |        | `(a ^ b) ^ c == a ^ (b ^ c)`      |

| Step | num | result = result ^ num | result value |
| ---- | --- | --------------------- | ------------ |
| 1    | 4   | 0 ^ 4                 | 4            |
| 2    | 1   | 4 ^ 1                 | 5            |
| 3    | 2   | 5 ^ 2                 | 7            |
| 4    | 1   | 7 ^ 1                 | 6            |
| 5    | 2   | 6 ^ 2                 | 4            |

How 7 ^ 1 is 6

Step 1: Convert to Binary

| Decimal | Binary |
| ------- | ------ |
| 7       | `0111` |
| 1       | `0001` |

Step 2: Apply XOR (bit-by-bit)

   0111   (7)
^  0001   (1)
--------
   0110   (6)

How XOR Works:

| Bit A | Bit B | A ^ B |
| ----- | ----- | ----- |
| 0     | 0     | 0     |
| 1     | 1     | 0     |
| 1     | 0     | 1     |
| 0     | 1     | 1     |

Final Result:
0110 in binary is 6 in decimal.

✅ So 7 ^ 1 = 6.
'''

