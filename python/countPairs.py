class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        
        """
        A good meal is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two.

You can pick any two different foods to make a good meal.

Given an array of integers deliciousness where deliciousness[i] is the deliciousness of the i​​​​​​th​​​​​​​​ item of food, return the number of different good meals you can make from this list modulo 109 + 7.

Note that items with different indices are considered different even if they have the same deliciousness value.
        """
        
        possiblesum = [pow(2,i) for i in range(22,-1,-1)]
        
        cnt = collections.Counter(deliciousness)
        ans = 0
        for val, count in cnt.items():
            
            for onesum in possiblesum:
                if onesum<val*2:
                    break
                    
                if onesum-val in cnt:
                    if val==onesum-val:
                        ans += count*(count-1)/2
                    else:
                        ans += count*cnt[onesum-val]
        return int(ans%(10**9+7))