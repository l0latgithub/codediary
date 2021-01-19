class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        
        """
        Given an array points containing the coordinates of points on a 2D plane, 
        sorted by the x-values, where points[i] = [xi, yi] such that xi < xj for 
        all 1 <= i < j <= points.length. You are also given an integer k.

        Find the maximum value of the equation yi + yj + |xi - xj|
        where |xi - xj| <= k and 1 <= i < j <= points.length. 
        It is guaranteed that there exists at least one pair of points that 
        satisfy the constraint |xi - xj| <= k.
        """
        
        minq = []
        
        ans = -float('inf')
        for x, y in points:
            
            while minq and x - minq[0][1]>k:
                heapq.heappop(minq)
            if minq:
                ans = max(ans, x+y-minq[0][0])
            heapq.heappush(minq, (x-y, x) )
            
        return ans