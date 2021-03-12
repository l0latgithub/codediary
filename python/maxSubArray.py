class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        """
        Given an integer array nums, find the contiguous subarray 
        (containing at least one number) which has the largest sum and return its sum.
        """
        
        if len(nums)<1:
            return 0
        
        runsum,maxsum = nums[0],nums[0]
        
        for val in nums[1:]:
            runsum = max(runsum+val, val)
            maxsum = max(runsum, maxsum)
        return maxsum