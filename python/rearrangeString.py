class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        
        """
        Given a non-empty string s and an integer k, 
        rearrange the string such that the same characters 
        are at least distance k from each other.

        All input strings are given in lowercase letters. 
        If it is not possible to rearrange the string, return an empty string "".
        
        The following 3 questions are the same on leetcode.com
        https://leetcode.com/problems/rearrange-string-k-distance-apart/
        https://leetcode.com/problems/reorganize-string/submissions/
        https://leetcode.com/problems/task-scheduler/
        Though k could be 0 in special case
        
        """
        if k==0:
            return s
        cnt = collections.Counter(s)
        
        maxcnt = max(cnt.values())
        num_maxcnt = list(cnt.values()).count(maxcnt)
        if (k*(maxcnt-1)+num_maxcnt) > len(s):
            return ""
        
        nlen = len(s)
        i = 0
        ans = list(s)
        for key, count in sorted(cnt.items(), key=lambda x:-x[1]):
            for _ in range(count):
                ans[i] = key
                i += k
                if i>=nlen:
                    i = (i-1)%k
        return "".join(ans)