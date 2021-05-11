class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # mapping { prevChar: newChar }
        # mapping { newChar: prevChar }
        m1 = {}
        m2 = {}
        
        for i in range(len(s)):
            # check if s[i] maps to t[i]
            if s[i] in m1 and m1[s[i]] != t[i]:
                return False
            # check if t[i] maps to s[i]
            if t[i] in m2 and m2[t[i]] != s[i]:
                return False
            # add the new mapping
            m1[s[i]] = t[i]
            m2[t[i]] = s[i]
        
        return True
                
