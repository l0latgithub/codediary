class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        """
        Given a string S, return the number of substrings of 
        length K with no repeated characters.
        """
        ans = 0
        
        seen = set()
        
        lo = 0
        for hi, char in enumerate(S):
            
            while char in seen:
                seen.remove(S[lo])
                lo+=1
            seen.add(char)
            if hi-lo+1>=K:
                ans+=1
        return ans