class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        """
        Given two arrays, write a function to compute their intersection.
        """
        
        s1cnt = collections.Counter(nums1)
        s2cnt = collections.Counter(nums2)
        
        if len(s1cnt)<len(s2cnt):
            return self.inter(s1cnt, s2cnt)
        else:
            return self.inter(s2cnt, s1cnt)
    
    def inter(self, s1, s2):
        ans = []
        # print (s1,s2)
        for key,cnt in s1.items():
            if key in s2:
                # print (key)
                ans.append(key)
        return ans

#         nums1.sort()
#         nums2.sort()
        
#         i1,i2=0,0
#         ans = []
#         while i1<len(nums1) and i2<len(nums2):
#             if nums1[i1]==nums2[i2]:
#                 ans.append(nums1[i1])
#                 while i1<(len(nums1)-1) and nums1[i1]==nums1[i1+1]:
#                     i1+=1
#                 i1+=1
#                 while i2<(len(nums2)-1) and nums2[i2]==nums2[i2+1]:
#                     i2+=1
#                 i2+=1
#             elif nums1[i1]<nums2[i2]:
#                 i1+=1
#             else:
#                 i2+=1
#         return ans
    