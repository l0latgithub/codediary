class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Given an array nums, write a function to move all 0's to the end
        of it while maintaining the relative order of the non-zero elements.
        
        Do not return anything, modify nums in-place instead.
        """
        
        nonzeroidx = 0
        
        for idx, val in enumerate(nums):
            if val!=0:
                nums[nonzeroidx],nums[idx]=nums[idx],nums[nonzeroidx]
                nonzeroidx+=1
                