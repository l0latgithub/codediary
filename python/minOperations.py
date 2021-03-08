class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        """
        You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it's possible, otherwise, return -1
        """
        
#         runsum = sum(nums)
        
#         lo, ans = 0, len(nums)+1
        
#         for hi, val in enumerate(nums):
#             runsum-=val
            
#             while lo<=hi and runsum<x:
#                 runsum+=nums[lo]
#                 lo+=1
            
#             if runsum==x:
#                 ans = min(ans, len(nums)-(hi-lo+1))
#         if ans<(len(nums)+1):
#             return ans
#         else:
#             return -1

        target = sum(nums)-x
    
        runsum, lo, ans = 0, 0, -1
        
        for hi, val in enumerate(nums):
            
            runsum += val
            while lo<=hi and runsum>target:
                runsum -= nums[lo]
                lo+=1
            
            if runsum==target:
                ans = max(ans, hi-lo+1)
                
        if ans==-1:
            return ans
        else:
            return len(nums)-ans