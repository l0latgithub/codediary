class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        """
        Given an integer array arr, return the length of 
        a maximum size turbulent subarray of arr.

        A subarray is turbulent if the comparison sign 
        flips between each adjacent pair of elements in the subarray.

        More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] 
        of arr is said to be turbulent if and only if:

        For i <= k < j:
        arr[k] > arr[k + 1] when k is odd, and
        arr[k] < arr[k + 1] when k is even.
        Or, for i <= k < j:
        arr[k] > arr[k + 1] when k is even, and
        arr[k] < arr[k + 1] when k is odd.
        """
        
        # solution 1
        if len(arr)<2:
            return len(arr)
        arrlen = len(arr)
        ans, lo = 1,0
        
        for hi in range(arrlen):
            if hi ==0 or arr[hi]==arr[hi-1]:
                lo = hi
            elif hi == (arrlen-1) or (arr[hi]-arr[hi-1])*(arr[hi]-arr[hi+1])<=0:
                ans = max(ans, hi-lo+1)
                lo = hi
        return ans

        # SOlution 2
#         if len(arr)<2:
#             return len(arr)
#         arrlen = len(arr)

#         anslen, runlen = 1,0
#         for i in range(arrlen):
#             if i>=2 and (arr[i-1]-arr[i-2])*(arr[i-1]-arr[i])>0:
#                 runlen += 1
#             elif i>=1 and arr[i]!=arr[i-1]:
#                 runlen = 2
#             else:
#                 runlen = 1
#             anslen = max(anslen, runlen)
#         return anslen