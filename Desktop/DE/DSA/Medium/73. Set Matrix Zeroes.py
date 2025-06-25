'''
73. Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

'''

def setMatrixtoZero1(matrix):

    # print(len(m), len(m[0]))

    zero_rows = set()
    zero_cols = set()
    
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 0:
                zero_rows.add(r)
                zero_cols.add(c)

    for r in zero_rows:
        for c in range(len(matrix[0])):
            print(r, c)
            matrix[r][c] = 0

    for c in zero_cols:
        for r in range(len(matrix)):
            matrix[r][c] = 0

    print(matrix)
            
                


matrix = [[0,1,1],[1,0,1],[1,1,1]]

'''
0 1 1
1 0 1
1 1 1

0 0 0
0 0 0
0 0 1
'''

op = setMatrixtoZero(matrix)