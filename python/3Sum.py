class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        """
        Given an array nums of n integers, are there elements 
        a, b, c in nums such that a + b + c = 0? Find all unique 
        triplets in the array which gives the sum of zero.

        Notice that the solution set must not contain duplicate triplets.
        """
        nums.sort()
        numlen = len(nums)
        ans = []
        for i in range(numlen-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            j = i+1
            k = numlen-1
            
            while j<k:
                sum3 = nums[i]+nums[j]+nums[k]
                if sum3==0:
                    ans.append([nums[i],nums[j],nums[k]])
                    while j<k and nums[j]==nums[j+1]:
                        j+=1
                    j+=1
                    while j<k and nums[k]==nums[k-1]:
                        k-=1
                    k-=1
                elif sum3<0:
                    j+=1
                else:
                    k-=1
        return ans