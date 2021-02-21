class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.
        """
        
        i1, i2, idx = m-1, n-1, m+n-1
        
        while i2>=0:
            
            if nums2[i2]>nums1[i1] or i1<0:
                nums1[idx]=nums2[i2]
                i2-=1
            else:
                nums1[idx]=nums1[i1]
                i1-=1
            idx-=1