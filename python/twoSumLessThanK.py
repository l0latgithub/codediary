class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        
        """
        Given an array nums of integers and integer k, 
        return the maximum sum such that there exists i < j 
        with nums[i] + nums[j] = sum and sum < k. 
        If no i, j exist satisfying this equation, return -1.
        """
        
        maxsum = -1
        nums.sort()
        lo, hi = 0, len(nums)-1
        while lo<hi:
            sum2 = nums[lo]+nums[hi]
            
            if sum2<k:
                maxsum = max(maxsum, sum2)
                lo+=1
            else:
                hi-=1
        return maxsum