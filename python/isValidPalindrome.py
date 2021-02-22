class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        """
        Given a string s, determine if it is a palindrome, 
        considering only alphanumeric characters and ignoring cases.
        """
        
        lo,hi = 0, len(s)-1
        
        while lo<hi:
            
            while lo<hi and not s[lo].isalnum():
                lo+=1
            while lo<hi and not s[hi].isalnum():
                hi-=1
            
            if s[lo].lower() != s[hi].lower():
                return False
            lo+=1
            hi-=1
        else:
            return True