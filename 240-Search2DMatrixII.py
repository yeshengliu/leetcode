class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        def search(left, up, right, down):
            # sub matrix has no height or width
            if left > right or up > down:
                return False
            # target value is larger than maximum or smaller than minimum
            if target < matrix[up][left] or target > matrix[down][right]:
                return False

            mid = left + (right - left) // 2

            # locate the row s.t. matrix[row-1][mid] < target < matrix[row][mid]
            row = up
            while row <= down and matrix[row][mid] <= target:
                if target == matrix[row][mid]:
                    return True
                row += 1

            return search(left, row, mid - 1, down) or search(mid + 1, up, right, row - 1)

        return search(0, 0, len(matrix[0]) - 1, len(matrix) - 1)
    
    
