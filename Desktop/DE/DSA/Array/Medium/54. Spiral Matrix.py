'''
54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

[
    [1,2,3]
    [4,5,6]
    [7,8,9]
]

'''


def spiralMatrix(matrix):
    
    m = len(matrix)
    n = len(matrix[0])

    left = 0
    bottom = m
    top = 0
    right = n

    final_arr = []

    while top < bottom and left < right:


        for i in range(left, right):
            # print(left ,i)
            final_arr.append(matrix[top][i])

        top += 1
        
        for i in range(top, bottom):
            # print("===",i, right-1) 
            final_arr.append(matrix[i][right - 1])
        
        right -= 1

        if top < bottom:
            # print(right, left)
            for i in range(right-1, left-1, -1):
                # print("==",bottom-1, i)
                final_arr.append(matrix[bottom -1][i])

            bottom -= 1


        if left < right:
            for i in range(bottom-1, top-1, -1):
                final_arr.append(matrix[i][left])

            left += 1


    print(final_arr)

    
    


# matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]
spiralMatrix(matrix)
