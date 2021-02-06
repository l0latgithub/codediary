class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        """
        Given a string s that consists of only uppercase English letters, 
        you can perform at most k operations on that string.

        In one operation, you can choose any character of the string and 
        change it to any other uppercase English character.

        Find the length of the longest sub-string containing all repeating 
        letters you can get after performing the above operations.
        
        """
        
        chardict = {}
        
        maxfreq = 0
        
        lo
        for hi, char in enumerate(s):
            
            chardict[char]=chardict.get(char, 0)+1
            maxfreq = max(maxfreq, chardict[char])
            
            if hi-lo+1-maxfreq>k:
                chardict[s[lo]]-=1
                lo+=1
    
        return len(s)-lo