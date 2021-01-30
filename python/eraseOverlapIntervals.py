class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        """
        Given a collection of intervals, find the minimum number 
        of intervals you need to remove to make the rest of the 
        intervals non-overlapping.
        
        intervals is left inclusive and right exclusive
        
        Similar question or variations
        https://leetcode.com/problems/non-overlapping-intervals/
        
        The following is a similar question and intervals are left and right inclusive
        https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
        
        """
        
        if len(intervals)<2:
            return 0
        
        intervals.sort(key=lambda x:x[1])
        print (intervals)
        start,end = intervals[0][0], intervals[0][1]
        ans = 0
        for nxtstart, nxtend in intervals[1:]:
            # Find minimum overlapping and right exclusive
            # https://leetcode.com/problems/non-overlapping-intervals/
            if nxtstart>=end:
                end = nxtend
            else:
                ans += 1
            
            # Find overlapping interval and right inclusive
            # https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
            # if nxtstart>end:
            #     ans+=1
            #     end = nxtend
            
        return ans