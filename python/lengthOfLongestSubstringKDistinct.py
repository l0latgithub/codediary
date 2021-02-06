class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        """
        Given a string s and an integer k, return the length of
        the longest substring of s that contains at most k distinct characters.
        """
        
        chardict = {}
        
        ans,lo = 0,0
        for hi, char in enumerate(s):
            
            chardict[char] = hi
            
            if len(chardict)>k:
                idx_to_remove = min(chardict.values())
                del chardict[s[idx_to_remove]]
                lo = idx_to_remove+1
            ans = max(ans, hi-lo+1)
        return ans