class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        """
        Your are given an array of positive integers nums.

        Count and print the number of (contiguous) subarrays 
        where the product of all the elements in the subarray is less than k.
        """
        
        runprd = 1
        
        ans, lo = 0, 0
        for hi, val in enumerate(nums):
            runprd *=val
            
            while lo<=hi and runprd>=k:
                runprd/=nums[lo]
                lo+=1
            ans += hi-lo+1
        return ans