class Solution:
    def minSwaps(self, data: List[int]) -> int:
        
        """
        Given a binary array data, return the minimum number of swaps 
        required to group all 1’s present in the array together 
        in any place in the array.
        """
        
        numones = sum(data)
        if numones==len(data):
            return 0
        
        runsum = sum(data[:numones])
        if runsum==numones:
            return 0
        
        ans = numones-runsum
        for idx,val in enumerate(data[numones:], numones):
            runsum+=val-data[idx-numones]
            ans = min(ans, numones-runsum)
        return ans
            