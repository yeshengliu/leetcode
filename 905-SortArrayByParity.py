class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        """
        To achieve space complexity, we do in-place operation on the array
        We use double pointer to save time complexity to O(N)
        Having a pointer scanning from begining and the other pointer from
        the end
        If there is even/odd number should not be there, swap the value from
        two pointers
        """
        
        pointerA = 0
        pointerB = len(A) - 1
        
        while pointerA < pointerB:
            if A[pointerA] % 2 == 0:
                pointerA += 1
            elif A[pointerB] % 2 == 1:
                pointerB -= 1
            else:
                temp = A[pointerB]
                A[pointerB] = A[pointerA]
                A[pointerA] = temp
                pointerA += 1
                pointerB -= 1
        
        return A