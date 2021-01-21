class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        """
        Given an array of integers nums and an integer limit, 
        return the size of the longest non-empty subarray 
        such that the absolute difference between any two elements of 
        this subarray is less than or equal to limit.
        """
        
#         minq = collections.deque()
#         maxq = collections.deque()
        
#         lo, ans = 0, 0
#         for hi, val in enumerate(nums):
#             while minq and val<minq[-1]:
#                 minq.pop()
#             while maxq and val>maxq[-1]:
#                 maxq.pop()
                
#             minq.append(val)
#             maxq.append(val)
            
#             while minq and maxq and maxq[0]-minq[0]>limit:
#                 if nums[lo]==minq[0]:
#                     minq.popleft()
#                     # lo+=1
#                 if nums[lo]==maxq[0]:
#                     maxq.popleft()
#                     # lo+=1
#                 lo+=1
#             ans = max(ans, hi-lo+1)
#         return ans
        
        minq, maxq = [],[]
        
        ans, lo = 0,0
        for hi, val in enumerate(nums):
            heapq.heappush(maxq, [-val, hi])
            heapq.heappush(minq, [val, hi])
            while -maxq[0][0]-minq[0][0]>limit:
                lo = min(maxq[0][1], minq[0][1]) + 1
                while maxq[0][1]<lo:
                    heapq.heappop(maxq)
                while minq[0][1]<lo:
                    heapq.heappop(minq)
            ans = max(ans, hi-lo+1)
        return ans