class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Given a binary array, find the maximum number of consecutive
        1s in this array if you can flip at most one 0.
        """
        
        k,lo = 1,0
        for hi in range(len(nums)):
            
            k -= 1- nums[hi]
            
            if k<0:
                k += 1-nums[lo]
                lo+=1
        return len(nums)-lo
                