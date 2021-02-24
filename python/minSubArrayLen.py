class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        """
        Given an array of positive integers nums and a positive 
        integer target, return the minimal length of a contiguous 
        subarray [numsl, numsl+1, ..., numsr-1, numsr] of which 
        the sum is greater than or equal to target. If there is no such subarray, return 0 instead.
        """
        
        ans, runsum, lo = len(nums)+1, 0 ,0
        
        for hi, val in enumerate(nums):
            runsum+=val

            while runsum >= target:
                ans=min(ans, hi-lo+1)
                runsum -= nums[lo]
                lo+=1
        if ans<(len(nums)+1):
            return ans
        else:
            return 0