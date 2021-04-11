class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }
        
        for element in tokens:
            
            if element in operator:
                # Apply operation on top 2 numbers
                y = stack.pop()
                x = stack.pop()
                operation = operator[element]
                stack.append(operation(x, y))
            else:
                stack.append(int(element))
        
        # stack should only store one value which is the result
        return stack.pop()
