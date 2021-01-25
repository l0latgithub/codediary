class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        
        """
        A dieter consumes calories[i] calories on the i-th day. 

        Given an integer k, for every consecutive sequence of k days 
        (calories[i], calories[i+1], ..., calories[i+k-1] for all 0 <= i <= n-k), 
        they look at T, the total calories consumed during that sequence of k days
        (calories[i] + calories[i+1] + ... + calories[i+k-1]):

        If T < lower, they performed poorly on their diet and lose 1 point; 
        If T > upper, they performed well on their diet and gain 1 point;
        Otherwise, they performed normally and there is no change in points.
        Initially, the dieter has zero points. Return the total number of points 
        the dieter has after dieting for calories.length days.

        Note that the total points can be negative.
        """
        runsum = sum(calories[:k])
        ans = (runsum>upper)-(runsum<lower)
        
        for idx, val in enumerate(calories[k:],k):
            runsum +=val-calories[idx-k]
            ans += (runsum>upper)-(runsum<lower)
        return ans