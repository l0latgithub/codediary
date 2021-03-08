class Solution:
    def balancedString(self, s: str) -> int:
        """
        You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and 'R'.

A string is said to be balanced if each of its characters appears n/4 times where n is the length of the string.

Return the minimum length of the substring that can be replaced with any other string of the same length to make the original string s balanced.

Return 0 if the string is already balanced.
        
        """
        cnt = collections.Counter(s)
        
        tgtlen = len(s)//4
        
        repdict = {}
        for key, val in cnt.items():
            if val>tgtlen:
                repdict[key] = val-tgtlen
        
        if len(repdict)<1:
            return 0
        
        lo, ans = 0, len(s)
        for hi, char in enumerate(s):
            
            if char in repdict:
                repdict[char]-=1
            
            while lo<=hi and max(repdict.values())<=0:
                ans = min(ans, hi-lo+1)
                
                if s[lo] in repdict:
                    repdict[s[lo]]+=1
                lo+=1
        return ans