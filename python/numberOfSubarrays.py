class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        """
        Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.
        """
        
#         sumdict = {0:1}
        
#         ans, runsum = 0, 0
        
#         for val in nums:
#             runsum += val%2
            
#             if runsum-k in sumdict:
#                 ans += sumdict[runsum-k]
            
#             sumdict[runsum] = sumdict.get(runsum, 0)+1
#         return ans

        def atMost(k):
            res = i = 0
            for j in range(len(nums)):
                k -= nums[j] % 2
                while k < 0:
                    k += nums[i] % 2
                    i += 1
                res += j - i + 1
            return res

        return atMost(k) - atMost(k - 1)