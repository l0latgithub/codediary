class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        
        """
        You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a < b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].
        """
        
        fi, si = 0,0
        ans = []
        while fi<len(firstList) and si<len(secondList):
            
            left = max(firstList[fi][0], secondList[si][0])
            right = min(firstList[fi][1], secondList[si][1])
            
            if left<=right:
                ans.append([left,right])
                
            if firstList[fi][1]<=secondList[si][1]:
                fi+=1
            else:
                si+=1
        return ans