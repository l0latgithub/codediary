class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.
        """
        people.sort(reverse=True)
        
        lo, hi = 0, len(people)-1
        while lo<=hi:
            if people[lo]+people[hi]<=limit:
                hi-=1
            lo+=1
        return lo