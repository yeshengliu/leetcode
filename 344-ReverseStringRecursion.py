class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        length = len(s)
        
        def helper(idx):
            if idx > length / 2 - 1:
                return
            s[idx], s[length - idx -1] = s[length - idx - 1], s[idx]
            helper(idx + 1)
        
        helper(0)
        
        return s
                
        
