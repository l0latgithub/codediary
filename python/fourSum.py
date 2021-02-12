class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Given an array nums of n integers and an integer target, 
        are there elements a, b, c, and d in nums such that a + b + c + d = target? 
        Find all unique quadruplets in the array which gives the sum of target.

        Notice that the solution set must not contain duplicate quadruplets.
        """
        def sum2(nums, tgt):
            lo,hi=0,len(nums)-1
            
            outs = []
            while lo<hi:
                if lo>0 and nums[lo]==nums[lo-1]:
                    lo+=1
                    continue
                
                sum2 = nums[lo]+nums[hi]
                if sum2==tgt:
                    outs.append([nums[lo], nums[hi]])
                    while lo<hi and nums[lo]==nums[lo+1]:
                        lo+=1
                    lo+=1
                    while lo<hi and nums[hi]==nums[hi-1]:
                        hi-=1
                    hi-=1
                elif sum2<tgt:
                    lo+=1
                else:
                    hi-=1
            return outs
        
        def dfs(nums, tgt, comb, results,k):
            
            if len(nums) < k or nums[0]*k>tgt or nums[-1]*k<tgt:
                return
            
            if k==2:
                outputs = sum2(nums, tgt)
                if outputs:
                    for out in outputs:
                        results.append(comb + out)
                return results
            
            for idx, val in enumerate(nums):
                if idx>0 and nums[idx]==nums[idx-1]:
                    continue
                dfs(nums[idx+1:],tgt-val, comb+[val], results, k-1)

        
        nums.sort()
        results = []
        k=4
        dfs(nums, target, [], results,k)
        return results