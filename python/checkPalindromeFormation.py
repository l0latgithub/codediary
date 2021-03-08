class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        
        """
        You are given two strings a and b of the same length. Choose an index and split both strings at the same index, splitting a into two strings: aprefix and asuffix where a = aprefix + asuffix, and splitting b into two strings: bprefix and bsuffix where b = bprefix + bsuffix. Check if aprefix + bsuffix or bprefix + asuffix forms a palindrome.

When you split a string s into sprefix and ssuffix, either ssuffix or sprefix is allowed to be empty. For example, if s = "abc", then "" + "abc", "a" + "bc", "ab" + "c" , and "abc" + "" are valid splits.

Return true if it is possible to form a palindrome string, otherwise return false.

Notice that x + y denotes the concatenation of strings x and y.
        """
        
        lo, hi = 0, len(a)-1
        
        while lo<hi and a[lo]==b[hi]:
            lo+=1
            hi-=1
        s1, s2 = a[lo:hi+1], b[lo:hi+1]
        
        lo, hi = 0, len(a)-1
        while lo<hi and b[lo]==a[hi]:
            lo+=1
            hi-=1
        s3, s4 = b[lo:hi+1], a[lo:hi+1]
        
        return any( subs==subs[::-1] for subs in (s1,s2,s3,s4) )