class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        """
        Given an array of integers numbers that is already 
        sorted in ascending order, find two numbers such that 
        they add up to a specific target number.

        Return the indices of the two numbers (1-indexed) as 
        an integer array answer of size 2, 
        where 1 <= answer[0] < answer[1] <= numbers.length.

        You may assume that each input would have exactly one 
        solution and you may not use the same element twice.
        """
        
        lo, hi = 0, len(numbers)-1
        
        while lo<hi:
            sum2 = numbers[lo]+numbers[hi]
            
            if sum2==target:
                return [lo+1, hi+1]
            elif sum2<target:
                lo+=1
            else:
                hi-=1