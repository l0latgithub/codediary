class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        """
        You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.
        """
        
#         arrlen = len(arr)
#         if arrlen<3:
#             return 0
#         ans = 0
        
#         for i in range(1, arrlen-1):
            
#             if arr[i-1]<arr[i]>arr[i+1]:
#                 left = i-1
#                 right = i+1
#                 while left>0 and arr[left]>arr[left-1]:
#                     left-=1
#                 while right<(arrlen-1) and arr[right]>arr[right+1]:
#                     right+=1
#                 ans = max(ans, right-left+1)
        
#         return ans
        arrlen = len(arr)
        if arrlen<3:
            return 0
        ans, lo=0,0
        peak = False
        for hi in range(1, arrlen-1):
            if arr[hi-1]<arr[hi]<arr[hi+1]:
                continue
            elif arr[hi-1]<arr[hi]>arr[hi+1]:
                peak=True
                ans = max(ans, hi-lo+2)
            elif arr[hi-1]>arr[hi]>arr[hi+1] and peak==True:
                ans = max(ans, hi-lo+2)
            else:
                peak=False
                lo = hi
        return ans
            