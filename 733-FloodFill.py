class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        lengthRow = len(image)
        lengthCol = len(image[0])
        origColor = image[sr][sc]
        
        def helper(rowIndex, colIndex):
            # out of bounder
            if rowIndex > lengthRow - 1 or rowIndex < 0:
                return
            if colIndex > lengthCol - 1 or colIndex < 0:
                return
            
            # change the color if color match the original color
            if image[rowIndex][colIndex] == newColor:
                return
            elif image[rowIndex][colIndex] == origColor:
                image[rowIndex][colIndex] = newColor
                helper(rowIndex - 1, colIndex)
                helper(rowIndex + 1, colIndex)
                helper(rowIndex, colIndex - 1)
                helper(rowIndex, colIndex + 1)
            else:
                return
            
        helper(sr, sc)
        return image
            
        
