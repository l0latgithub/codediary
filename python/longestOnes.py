class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        
        """
        Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

        Return the length of the longest (contiguous) subarray that contains only 1s. 
        """
        
#         lo, ans = 0,0
        
#         for hi in range(len(A)):
            
#             K -= 1-A[hi]
            
#             if K<0:
#                 K += 1 - A[lo]
#                 lo+=1
#         return len(A)-lo
        
        lo, ans = 0,0
        numzeros = 0
        for hi in range(len(A)):
            
            if A[hi]==0:
                numzeros+=1
            
            while numzeros>K:
                numzeros -= 1 - A[lo]
                lo += 1
            
            ans = max(ans, hi-lo+1)
            
        return ans