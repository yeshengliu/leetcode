class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        output = [0] * len(T)
        stack = []
        
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                idx = stack.pop()
                output[idx] = i - idx
            
            stack.append(i)
            
        return output
