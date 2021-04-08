class Solution:
    def isValid(self, s: str) -> bool:
        # when detecting a left paranthese, put it in the stack
        # when detecting a right parantheses, remove the opposite from
        # the stack
        
        p = []
        mapping = {')': '(', ']': '[', '}': '{'}
        
        for c in s:
            if c in mapping:
                top_element = p.pop() if p else '#'
                
                if mapping[c] != top_element:
                    return False
            else:
                p.append(c)
            
        return not p
