class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        """
        Given a string s and a string array dictionary, return the longest
        string in the dictionary that can be formed by deleting some of the 
        given string characters. If there is more than one possible result, 
        return the longest word with the smallest lexicographical order. 
        If there is no possible result, return the empty string.
        """
        
#         dictionary = sorted(dictionary, key=lambda x:(-len(x),x))
        
#         for word in dictionary:
#             last = 0
#             for char in word:
#                 last = s.find(char,last)+1
#                 if last==0:
#                     break
#             else:
#                 return word
#         else:
#             return ""
#         dictionary.sort(key=lambda x:(-len(x),x))
        
#         for word in dictionary:
#             last = 0
#             for char in word:
#                 last = s.find(char,last)+1
#                 if last==0:
#                     break
#             else:
#                 return word
#         else:
#             return ""

        dictionary.sort(key=lambda x:(-len(x),x))
        
        for word in dictionary:
            s_it = iter(s)
            if all(char in s_it for char in word):
                return word
        else:
            return ""