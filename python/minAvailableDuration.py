class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        
        """
        Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the earliest time slot that works for both of them and is of duration duration.

If there is no common time slot that satisfies the requirements, return an empty array.

The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.

It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.
        """
        
        slots1.sort()
        slots2.sort()
        i1, i2=0,0
        
        while i1<len(slots1) and i2<len(slots2):
            
            start = max(slots1[i1][0], slots2[i2][0])
            end = min(slots1[i1][1], slots2[i2][1])
            
            if end-start>=duration:
                return [start, start+duration]
            
            if slots1[i1][1]>slots2[i2][1]:
                i2+=1
            else:
                i1+=1
        return []