class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        """
        Implement strStr().

        Return the index of the first occurrence of needle 
        in haystack, or -1 if needle is not part of haystack.
        """
        
        if len(needle)>len(haystack):
            return -1
        elif needle==haystack:
            return 0
        elif needle=="":
            return 0
        
        pownum = 26
        
        haynum = [ord(char)-ord('a') for char in haystack]
        nednum = [ord(char)-ord('a') for char in needle]
        
        hayhash = 0
        nedhash = 0
        modnum = 10**9+7
        hlen, nlen = len(haystack), len(needle)
        for i in range(nlen):
            hayhash = ( haynum[i] + hayhash*pownum ) % modnum
            nedhash = ( nednum[i] + nedhash*pownum ) % modnum
        
        hashnum = pow(pownum, nlen, modnum)
        
        if hayhash==nedhash:
            return 0
        
        for i in range(1, hlen-nlen+1):
            hayhash = ( hayhash * pownum + haynum[i+nlen-1] - haynum[i-1]*hashnum ) % modnum
            # print (hayhash, nedhash)
            if nedhash==hayhash:
                return i
        else:
            return -1