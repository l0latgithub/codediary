class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        """
        Given a string s, find the length of the longest substring without repeating characters.
        """
        seen = {}
        lo, ans = 0, 0
        for hi, char in enumerate(s):
            
            if char in seen:
                lo = max(lo, seen[char]+1)
            ans = max(ans, hi-lo+1)
            seen[char] = hi
        return ans