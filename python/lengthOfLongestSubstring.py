class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string s, find the length of the longest substring without repeating characters.
        """
        # ans,lo = 0,0
        # seen = set()
        # for hi, char in enumerate(s):
        #     while char in seen:
        #         seen.remove(s[lo])
        #         lo+=1
        #     seen.add(char)
        #     ans = max(ans, hi-lo+1)
        # return ans
        ans,lo = 0,0
        seen = {}
        for hi, char in enumerate(s):
            if char in seen:
                # print (lo)
                lo = max(seen[char]+1, lo)
                # print (lo)
            seen[char]=hi
            ans = max(ans, hi-lo+1)
        return ans