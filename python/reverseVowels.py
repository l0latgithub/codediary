class Solution:
    def reverseVowels(self, s: str) -> str:
        
        """
        Write a function that takes a string as input and reverse only the vowels of a string.
        """
        lo, hi =0, len(s)-1
        slst = list(s)
        vowel = "aeiouAEIOU"
        while lo<hi:
            while lo<hi and slst[lo] not in vowel:
                lo+=1
            while lo<hi and slst[hi] not in vowel:
                hi-=1
            # print (lo, hi)
            slst[lo],slst[hi]=slst[hi],slst[lo]
            lo+=1
            hi-=1
        return "".join(slst)