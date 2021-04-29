class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        output = ""
        
        # process input string
        while s:
            char = s[0]
            s = s[1:]
            if char != "]":
                # push the char in the stack
                stack.append(char)
            else:
                # find the top '[' from the stack
                # combine all chars and push back to
                # the stack
                newString = ""
                topChar = stack.pop()
                while topChar != "[":
                    newString = topChar + newString
                    topChar = stack.pop()
                # we should expect a number after '['
                numRep = ""
                while stack and str.isdigit(stack[-1]):
                    numRep = stack.pop() + numRep
                numRep = int(numRep)
                stack.append(newString * numRep)
        
        # combine chars / strings from the stack
        while stack:
            output = stack.pop() + output
        
        return output
