class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        
        """
        In an array A of 0s and 1s, how many non-empty subarrays have sum S?
        """
        
        sumdict ={0:1}
        
        ans,runsum = 0,0
        for val in A:
            runsum+=val
            if runsum - S in sumdict:
                ans += sumdict[runsum-S]
            sumdict[runsum] = sumdict.get(runsum,0)+1
        print (sumdict)
        return ans