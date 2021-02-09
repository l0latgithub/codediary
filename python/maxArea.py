class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        """
        Given n non-negative integers a1, a2, ..., an , where each represents 
        a point at coordinate (i, ai). n vertical lines are drawn such that 
        the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, 
        which, together with the x-axis forms a container, such that the container 
        contains the most water.
        """
        
        maxvol = 0
        
        lo, hi = 0, len(height)-1
        while lo<hi:
            if height[lo]<height[hi]:
                maxvol = max(maxvol, height[lo]*(hi-lo))
                lo+=1
            else:
                maxvol = max(maxvol, height[hi]*(hi-lo))
                hi-=1
        return maxvol