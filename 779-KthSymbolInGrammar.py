class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # if k is in the first half, it is the same as k-th element
        # in row(n-1)
        # if k is in the second half, it is the complement of
        # k - 2^(n-1)-th element in row(n-1)
        
        if n == 1:
            return 0
        
        half = 2 ** (n - 2)
        
        if k <= half:
            return self.kthGrammar(n - 1, k)
        
        res = self.kthGrammar(n - 1, k - half)
        if res == 0:
            return 1
        else:
            return 0
