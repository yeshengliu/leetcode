class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        # 1. Do a transpose
        for i in range(n):
            for j in range(i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        # 2. Do a horizontal flip
        for i in range(n):
            for j in range(n // 2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][n - j - 1]
                matrix[i][n - j - 1] = temp
        
