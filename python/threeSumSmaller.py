class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        """
        Given an array of n integers nums and an integer target, 
        find the number of index triplets i, j, k with 
        0 <= i < j < k < n that satisfy the condition 
        nums[i] + nums[j] + nums[k] < target.
        """
        
        nums.sort()
        ans = 0
        for i in range(len(nums)-2):
            
            j = i+1
            k = len(nums)-1
            
            while j<k:
                sum3 = nums[i]+nums[j]+nums[k]
                if sum3<target:
                    ans += k-j
                    j+=1
                else:
                    k-=1
        return ans
                