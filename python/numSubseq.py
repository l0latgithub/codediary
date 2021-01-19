class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        """
        Given an array of integers nums and an integer target.

        Return the number of non-empty subsequences of nums such 
        that the sum of the minimum and maximum element on it is
        less or equal to target. Since the answer may be too large, 
        return it modulo 10^9 + 7.
        """
        
        nums.sort()
        lo, hi = 0, len(nums)-1
        modnum, ans = 10**9+7, 0
        while lo<=hi:
            
            if nums[lo]+nums[hi]<=target:
                ans += pow(2, hi-(lo+1)+1, modnum)
                lo+=1
            else:
                hi-=1
        return ans % modnum