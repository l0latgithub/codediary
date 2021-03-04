class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        """
        A string S of lowercase English letters is given. We want to
        partition this string into as many parts as possible so that
        each letter appears in at most one part, and return a list of 
        integers representing the size of these parts.
        """
        
#         last = {char:idx for idx, char in enumerate(S)}
        
#         lo,hi = 0,0
#         ans = []
#         for idx, char in enumerate(S):
            
#             hi = max(hi, last[char])
            
#             if hi==idx:
#                 ans.append(hi-lo+1)
#                 lo=hi+1
#         return ans

        interval = {}
        for idx, char in enumerate(S):
            
            if char in interval:
                interval[char][-1]=idx
            else:
                interval[char]=[idx,idx]
            
        start,end=0,0
        ans = []
        for nxtstart, nxtend in interval.values():
            if end==0 or nxtstart>end:
                start=nxtstart
                end = nxtend
                ans.append(end-start+1)
            else:
                end=max(end, nxtend)
                ans[-1] = end-start+1
        return ans