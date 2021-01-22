class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arrSet = {}
        
        for num in arr:
            if num * 2 in arrSet.keys():
                return True
            if num / 2 in arrSet.keys():
                return True
            arrSet[num] = 1
        
        return False