class Solution:
    def jump(self, nums: List[int]) -> int:
        
        """
        Given an array of non-negative integers nums, 
        you are initially positioned at the first index of the array.

        Each element in the array represents your maximum jump length at that position.

        Your goal is to reach the last index in the minimum number of jumps.

        Will check whether you can reach the end, there is a corner case when lenngth=1
        
        At this case, you are at the end without jumping
        """
        
        if len(nums)<2:
            return 0
        # If jump array only has one element when asking you whether can reach the end
        # if len(nums)<2:
        #     return True

        curEnd, maxPos = 0, 0
        jump = 0
        for idx, val in enumerate(nums[:-1]):
            
            if idx>maxPos:
                return False
            maxPos = max(maxPos, idx+val)
            
            if idx==curEnd:
                jump+=1
                curEnd = maxPos
            
            if curEnd>=(len(nums)-1):
                return jump
            
        if maxPos>=(len(nums)-1):
            return jump
        else:
            return False