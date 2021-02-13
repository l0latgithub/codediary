class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Given a sorted array nums, remove the duplicates in-place 
        such that each element appears only once and returns the new length.

        Do not allocate extra space for another array, you must do this
        by modifying the input array in-place with O(1) extra memory.
        """
        numlen = len(nums)
        if numlen<2:
            return numlen
        
        i = 1
        for j in range(1,numlen):
            if nums[j]!=nums[i-1]:
                nums[i]=nums[j]
                i+=1
        return i