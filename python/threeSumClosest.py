class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        """
        Given an array nums of n integers and an integer target, 
        find three integers in nums such that the sum is closest to target. 
        Return the sum of the three integers. You may assume that each 
        input would have exactly one solution.
        """
        nums.sort()
        numlen = len(nums)
        ans = float('inf')
        
        for i in range(numlen-2):
            
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            j = i+1
            k = numlen-1
            while j<k:
                sum3 = nums[i]+nums[j]+nums[k]
                if sum3==target:
                    return target
                elif sum3<target:
                    j+=1
                else:
                    k-=1
                if abs(sum3-target)<abs(ans-target):
                    ans = sum3
        return ans