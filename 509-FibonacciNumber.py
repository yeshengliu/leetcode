class Solution:
    def fib(self, n: int) -> int:
        results = {}
        results[0] = 0
        results[1] = 1
        
        def helper(n):
            if n in results:
                return results[n]
            return helper(n - 1) + helper(n - 2)
        
        return helper(n)
