class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Given an array nums with n objects colored red, white, or blue,
        sort them in-place so that objects of the same color are adjacent, 
        with the colors in the order red, white, and blue.

        We will use the integers 0, 1, and 2 to represent the color 
        red, white, and blue, respectively.
        """
        
        red, white, blue = 0,0,len(nums)-1
        
        while white<=blue:
            if nums[white]==2:
                nums[white],nums[blue]=nums[blue], nums[white]
                blue-=1
            elif nums[white]==0:
                nums[red],nums[white]=nums[white],nums[red]
                red+=1
                white+=1
            else:
                white+=1