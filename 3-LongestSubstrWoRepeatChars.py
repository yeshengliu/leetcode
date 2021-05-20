class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        mp = {}     # value - index pair
        left = 0
        ans = 0
        
        for right in range(len(s)):
            if s[right] in mp:
                # update left
                left = max(left, mp[s[right]] + 1)
            
            # update hashmap
            mp[s[right]] = right
            # update ans
            ans = max(ans, right - left + 1)
        
        return ans
