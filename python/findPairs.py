class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        """
        Given an array of integers nums and an integer k, 
        return the number of unique k-diff pairs in the array.

        A k-diff pair is an integer pair (nums[i], nums[j]), 
        where the following are true:

        0 <= i, j < nums.length
        i != j
        |nums[i] - nums[j]| == k
        
        Notice that |val| denotes the absolute value of val.
        """
#         cnt = collections.Counter(nums)
        
#         if k==0:
#             return sum(val>=2 for key,val in cnt.items())
#         else:
#             ans = 0
#             for key in cnt.keys():
#                 if key-k in cnt:
#                     ans += 1
#             return ans

        nums.sort()
    
        lo,hi = 0, 1
        ans = 0
        
        while hi<len(nums):
            diff = nums[hi]-nums[lo] - k
            if diff<0 or lo>=hi:
                hi+=1
            elif diff>0 or (lo>0 and nums[lo]==nums[lo-1]):
                lo+=1
            else:
                ans+=1
                lo+=1
        return ans