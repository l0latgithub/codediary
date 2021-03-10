class Solution:
    def jump(self, nums: List[int]) -> int:
        
        """
        Given an array of non-negative integers nums, 
        you are initially positioned at the first index of the array.

        Each element in the array represents your maximum jump length at that position.

        Your goal is to reach the last index in the minimum number of jumps.

        """
        
        maxJump, jump = 0,0
        lastJumpPos = 0
        for idx, val in enumerate(nums[:-1]):
            if idx>maxJump:
                return False
            
            maxJump = max(maxJump, idx+val)
            
            if idx==lastJumpPos:
                jump+=1
                lastJumpPos = maxJump
        
        if maxJump>=len(nums)-1:
            return jump
        else:
            return False