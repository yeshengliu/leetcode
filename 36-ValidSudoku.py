class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check all rows
        for row in board:
            hashset = set()
            for i in range(9):
                val = row[i]
                if val != "." and val in hashset:
                    return False
                hashset.add(val)
            
        # check all columns
        for colIndex in range(9):
            hashset = set()
            for rowIndex in range(9):
                val = board[rowIndex][colIndex]
                if val != "." and val in hashset:
                    return False
                hashset.add(val)
        
        # check 3 * 3 sub-boxes
        def isValidSubBoxes(rowIndex, colIndex):
            hashset = set()
            for i in range(3):
                for j in range(3):
                    val = board[rowIndex + i][colIndex + j]
                    if val != "." and val in hashset:
                        return False
                    hashset.add(val)
            return True
        
        for i in range(3):
            for j in range(3):
                if not isValidSubBoxes(i * 3, j * 3):
                    return False
        
        return True
