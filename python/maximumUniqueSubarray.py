class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        
        """
        You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).
        """
        
        runsum, maxsum = 0,0
        seen = set()
        lo = 0
        
        for hi, val in enumerate(nums):
            
            while lo<=hi and val in seen:
                seen.remove(nums[lo])
                runsum -= nums[lo]
                lo+=1
            seen.add(val)
            runsum += val
            maxsum = max(runsum, maxsum)
        return maxsum
        
        