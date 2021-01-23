class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        """
        You are given two strings s and t of the same length. 
        You want to change s to t. Changing the i-th character 
        of s to i-th character of t costs |s[i] - t[i]| that is,
        the absolute difference between the ASCII values of the characters.

        You are also given an integer maxCost.

        Return the maximum length of a substring of s that 
        can be changed to be the same as the corresponding 
        substring of twith a cost less than or equal to maxCost.

        If there is no substring from s that can be changed to 
        its corresponding substring from t, return 0.
        """
#         runcost, lo, ans = 0, 0, 0
        
#         for hi in range(len(s)):
#             runcost += abs( ord(s[hi]) -ord(t[hi]) )
            
#             while runcost>maxCost:
#                 runcost -= abs( ord(s[lo]) -ord(t[lo]) )
#                 lo+=1
            
#             ans = max(ans, hi-lo+1)
#         return ans

        runcost, lo, ans = 0, 0, 0
        
        for hi in range(len(s)):
            runcost += abs( ord(s[hi]) -ord(t[hi]) )
            
            if runcost>maxCost:
                runcost -= abs( ord(s[lo]) -ord(t[lo]) )
                lo+=1
            
        return len(s)-lo
        
        