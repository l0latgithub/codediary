class Solution:
    def trap(self, height: List[int]) -> int:
        
        """
        Given n non-negative integers representing an elevation 
        map where the width of each bar is 1, compute how much 
        water it can trap after raining.
        """
        
        if len(height)<3:
            return 0
        
        leftmost = height[0]
        rightmost = height[-1]
        
        lo,hi=0, len(height)-1
        ans = 0
        while lo<hi:
            
            leftmost = max(leftmost, height[lo])
            rightmost = max(rightmost, height[hi])
            
            if leftmost<rightmost:
                ans += leftmost-height[lo]
                lo+=1
            else:
                ans += rightmost-height[hi]
                hi-=1
        return ans