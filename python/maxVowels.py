class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        """
        Given a string s and an integer k.

        Return the maximum number of vowel letters in any substring of s with length k.

        Vowel letters in English are (a, e, i, o, u).
        
        s consists of lowercase English letters.
        """
        
        ans, run = 0,0
        vowel = "aeiou"
        for idx, char in enumerate(s):
            
            if char in vowel:
                run+=1
            
            if idx>=k:
                if s[idx-k] in vowel:
                    run-=1
            ans = max(ans, run)
        return ans