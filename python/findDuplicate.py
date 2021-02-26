class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Given an array of integers nums containing n + 1 integers 
        where each integer is in the range [1, n] inclusive.

        There is only one repeated number in nums, return this repeated number.
        """
        
#         for val in nums:
            
#             if nums[abs(val)]>0:
#                 nums[abs(val)]*=-1
#             else:
#                 return abs(val)

        fast = nums[0]
        slow = nums[0]
        
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            
            if fast==slow:
                break
        
        fast = nums[0]
        while fast!=slow:
            fast = nums[fast]
            slow = nums[slow]
        
        return fast