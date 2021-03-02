class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        """
        You are playing a game involving a circular array of non-zero integers nums. 
        Each nums[i] denotes the number of indices forward/backward you must move 
        if you are located at index i:

        If nums[i] is positive, move nums[i] steps forward, and
        If nums[i] is negative, move nums[i] steps backward.
        Since the array is circular, you may assume that moving forward from 
        the last element puts you on the first element, and moving backwards 
        from the first element puts you on the last element.

        A cycle in the array consists of a sequence of indices seq of length k where:

        . Following the movement rules above results in the repeating index sequence
        seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
        . Every nums[seq[j]] is either all positive or all negative.
        . k > 1
        
        Return true if there is a cycle in nums, or false otherwise.
        """
        numlen = len(nums)
        seen = [0]*numlen
        
        for idx, val in enumerate(nums):
            
            thistrip = set()
            while seen[idx]==0:
                thistrip.add(idx)
                seen[idx]=1
                
                nxt_idx = (idx+nums[idx])%numlen
                
                if idx==nxt_idx or val*nums[nxt_idx]<=0:
                    break
                
                if nxt_idx in thistrip:
                    return True
                
                idx=nxt_idx
        else:
            return False