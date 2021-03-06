class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        """
        Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
        """
        
        # lo,hi = 0, len(nums)-1
        # ans = []
        # while lo<=hi:
        #     if abs(nums[lo])>abs(nums[hi]):
        #         ans.append(nums[lo]**2)
        #         lo+=1
        #     else:
        #         ans.append(nums[hi]**2)
        #         hi-=1
        # return ans[::-1]
        lo,hi = 0, len(nums)-1
        ans = [0]*len(nums)
        while lo<=hi:
            lopow2 = nums[lo]**2
            hipow2 = nums[hi]**2
            if lopow2>hipow2:
                ans[hi-lo]=lopow2
                lo+=1
            else:
                ans[hi-lo]=hipow2
                hi-=1
        return ans
    