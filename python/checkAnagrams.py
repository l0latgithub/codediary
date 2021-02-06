class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        """
        Given two strings s1 and s2, write a function to return true 
        if s2 contains the permutation of s1. In other words, 
        one of the first string's permutations is the substring of the second string.
        
        Same question
        https://leetcode.com/problems/permutation-in-string
        https://leetcode.com/problems/find-all-anagrams-in-a-string
        
        """
        
        nums1 = [ord(char)-ord('a') for char in s1]
        nums2 = [ord(char)-ord('a') for char in s2]
        
        target = [0]*26
        tgtlen = len(nums1)
        for num in nums1:
            target[num]+=1
        
        runwin = [0]*26
        for idx,num in enumerate(nums2):
            runwin[num]+=1
            if idx>=tgtlen:
                runwin[nums2[idx-tgtlen]]-=1
            if target==runwin:
                return True
        else:
            return False