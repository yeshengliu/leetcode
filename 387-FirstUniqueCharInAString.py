class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        charCount = {}
        
        for i in range(len(s)):
            
            c = s[i]
            
            if c in charCount:
                charCount[c][1] += 1
            else:
                charCount[c] = [i, 1]
        
        index = []
        for c in charCount:
            if charCount[c][1] == 1:
                index.append(charCount[c][0])
        
        return min(index) if index else -1
                
