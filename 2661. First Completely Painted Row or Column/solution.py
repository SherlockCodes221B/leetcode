'''
You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].

Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].

Return the smallest index i at which either a row or a column will be completely painted in mat.

 

Example 1:

image explanation for example 1
Input: arr = [1,3,4,2], mat = [[1,4],[2,3]]
Output: 2
Explanation: The moves are shown in order, and both the first row and second column of the matrix become fully painted at arr[2].
Example 2:

image explanation for example 2
Input: arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]
Output: 3
Explanation: The second column becomes fully painted at arr[3].


'''

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        num_rows, num_cols = len(mat), len(mat[0])
        row_count, col_count = [0] * num_rows, [0] * num_cols
        num_to_pos = {}

        # Create a map to store the position of each number in the matrix
        for row in range(num_rows):
            for col in range(num_cols):
                num_to_pos[mat[row][col]] = [row, col]

        for i in range(len(arr)):
            num = arr[i]
            row, col = num_to_pos[num]

            # Increment the count for the corresponding row and column
            row_count[row] += 1
            col_count[col] += 1

            # Check if the row or column is completely painted
            if row_count[row] == num_cols or col_count[col] == num_rows:
                return i

        # This line will never be reached as per the problem statement
        return -1
