class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        length = len(arr)
        ans = 1
        start = 0
        
        def cmp(a, b):
            if a == b:
                return 0
            return 1 if a > b else -1
        
        for i in range(1, length):
            c = cmp(arr[i - 1], arr[i])
            # update start if adjacent integers are same
            if c == 0:
                start = i
            # update ans if reach the end or not fulfill sign flip
            elif i == length - 1 or c * cmp(arr[i], arr[i + 1]) != -1:
                ans = max(ans, i - start + 1)
                start = i
        
        return ans
                
            
            
        
