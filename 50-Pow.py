class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(n):
            if n == 0:
                return 1
            if n % 2 == 0:
                res = helper(n / 2)
                return res * res
            res = helper(n // 2)
            return res * res * x
            
        if n < 0:
            x = 1 / x
            n = -n
        
        return helper(n)
        
