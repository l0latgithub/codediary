class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        
        Write a function that reverses a string. The input 
        string is given as an array of characters char[].

        Do not allocate extra space for another array, you must 
        do this by modifying the input array in-place with O(1) extra memory.

        You may assume all the characters consist of printable ascii characters.
        """
        
        lo, hi =0, len(s)-1
        while lo<hi:
            s[lo],s[hi]=s[hi],s[lo]
            lo+=1
            hi-=1