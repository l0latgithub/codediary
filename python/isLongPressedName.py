class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        """
        Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.
        """
#         ni,ti=0,0
        
#         while ti<len(typed):
#             if ni<len(name) and name[ni]==typed[ti]:
#                 ni+=1
#                 ti+=1
#             elif ti>0 and typed[ti]==typed[ti-1]:
#                 ti+=1
#             else:
#                 return False
#             # print (ni, ti)
#         return ni==len(name) and ti==len(typed)

        ni = 0
        for ti in range(len(typed)):
            if ni<len(name) and name[ni]==typed[ti]:
                ni+=1
            elif ni==0 or typed[ti]!=typed[ti-1]:
                return False
        return ni==len(name)