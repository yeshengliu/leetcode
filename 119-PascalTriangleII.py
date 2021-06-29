class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        above = self.getRow(rowIndex - 1)
        curr = [1]
        
        for i in range(rowIndex - 1):
            curr.append(above[i] + above[i + 1])
        curr.append(1)
        
        return curr
            
