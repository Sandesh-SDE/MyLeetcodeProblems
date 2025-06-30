'''
2022. Convert 1D Array Into 2D Array
You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n. You are tasked with creating a 2-dimensional (2D) array with  m rows and n columns using all the elements from original.

The elements from indices 0 to n - 1 (inclusive) of original should form the first row of the constructed 2D array, the elements from indices n to 2 * n - 1 (inclusive) should form the second row of the constructed 2D array, and so on.

Return an m x n 2D array constructed according to the above procedure, or an empty 2D array if it is impossible.

 

Example 1:
--------------------
Input: original = [1,2,3,4], m = 2, n = 2
Output: [[1,2],[3,4]]
Explanation: The constructed 2D array should contain 2 rows and 2 columns.
The first group of n=2 elements in original, [1,2], becomes the first row in the constructed 2D array.
The second group of n=2 elements in original, [3,4], becomes the second row in the constructed 2D array.

Example 2:
--------------------
Input: original = [1,2,3], m = 1, n = 3
Output: [[1,2,3]]
Explanation: The constructed 2D array should contain 1 row and 3 columns.
Put all three elements in original into the first row of the constructed 2D array.

'''

# Best solution that i understoop
'''
step 1 : get the n value to know how many dimesion that you need to make
step 2: if n is 2 then use slice method from 0 
step 3: ex : [0:2] it will print index values 0 and 1 
step 4: so append values from orginal to new array accordingly
'''
def convertArray(arr, r, c):

    if r * c != len(arr):
        return None
    
    result = []
    for i in range(0,len(original),n):

        row = original[i:i+n] #slice according to the value of n each time.

        result.append(row)

    print(result)


def convertArray2(arr, r, c):

    if r * c != len(arr):
        return None
    
    result = []                        # Step 2
    for i in range(m):                 # Step 3
        row = original[i * n : (i + 1) * n]  # Step 4
        result.append(row)

    print(result)

def convertArray3(arr, r, c):

    op = []
    a = 0
    for r in range(r):

        rows = []
        j = 0
        
        while j < n:
            
            print(a, j)
            rows.append(arr[a])

            j += 1
            a += 1
          
        op.append(rows)

    print(op)





original = [1,2,3,4]
m = 2
n = 2

'''
1 2
3 4

[[1, 3], [3, 4]]
'''

op = convertArray(original,m , n)
