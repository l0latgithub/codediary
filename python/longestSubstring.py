class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        """
        Given a string s and an integer k, return the length of 
        the longest substring of s such that the frequency of 
        each character in this substring is greater than or equal to k.
        """
        # for char in s:
        #     if s.count(char)<k:
        #         return max(self.longestSubstring(subs, k) for subs in s.split(char))
        # else:
        #     return len(s)
        
        stack = [s]
        ans = 0
        while stack:
            string = stack.pop()
            
            for char in string:
                if string.count(char)<k:
                    stack.extend(subs for subs in string.split(char))
                    break
            else:
                ans = max(ans, len(string))
        return ans