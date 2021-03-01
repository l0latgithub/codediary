class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        
        """
        Given a sorted array of integers nums and integer values a, b and c.
        Apply a quadratic function of the form f(x) = ax2 + bx + c to 
        each element x in the array.

        The returned array must be in sorted order.

        Expected time complexity: O(n)
        """
        
        if a==0:
            for i in range(len(nums)):
                nums[i]=b*nums[i]+c
            
            if b<0:
                return nums[::-1]
            else:
                return nums
        
        else:
            symmetry = -b/2.0/a
            lo,hi = 0, len(nums)-1
            ans = []
            while lo<=hi:
                if abs(nums[lo]-symmetry)>abs(nums[hi]-symmetry):
                    ans.append(a*nums[lo]**2+b*nums[lo]+c)
                    lo+=1
                else:
                    ans.append(a*nums[hi]**2+b*nums[hi]+c)
                    hi-=1
            
            if a<0:
                return ans
            else:
                return ans[::-1]