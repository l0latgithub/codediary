class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        """
        Find all valid combinations of k numbers that sum up to n 
        such that the following conditions are true:

        Only numbers 1 through 9 are used.
        Each number is used at most once.
        Return a list of all possible valid combinations. 
        The list must not contain the same combination twice, 
        and the combinations may be returned in any order.
        
        combination sum I/II/III
        https://leetcode.com/problems/combination-sum-iii/
        
        Solution here is for combindation III, small changes are 
        comment below to make it work for combination sum I/II
        """
        
        def dfs(nums, comb, results, target, k):
            # print (nums)
            # k is used to determine how many number will be used
            # It is not necessary for I/II
            
            if target==0 and k==0:
                results.append(comb)
                return
            
            # It is not necessary for I/II
            if not nums or len(nums)<k or nums[0]*k>target or nums[-1]*k<target:
                return
            
            if target<0:
                return
            else:
                for idx, num in enumerate(nums):
                    if target<num:
                        return
                    if idx>0 and nums[idx]==nums[idx-1]:
                        continue
                    # use nums[idx:] when you are allowd to use the number more than once
                    dfs(nums[idx+1:], comb+[num], results, target-num, k-1)
        
        results = []
        candidates = list(range(1,10))
        dfs(candidates, [], results, n,k)
        return results