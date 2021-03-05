class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        """
        Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
        """
        def rmbackspace(s):
            
            slst = list(s)
            ans = []
            
            for char in slst:
                if char!="#":
                    ans.append(char)
                elif ans:
                    ans.pop()
            
            return "".join(ans)
        
        return rmbackspace(S)==rmbackspace(T)