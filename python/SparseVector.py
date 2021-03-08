class SparseVector:
    def __init__(self, nums: List[int]):
        
        # self.data = {}
        # for idx, val in enumerate(nums):
        #     if val > 0:
        #         self.data[idx]=val
        
        self.data = []
        for idx, val in enumerate(nums):
            if val > 0:
                self.data.append((idx,val))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        
        # ans = 0
        # for idx, val in self.data:
        #     if idx in vec.data:
        #         ans += self.data[idx]*vec.data[idx]
        # return ans
        
        ans = 0
        i1,i2=0,0
        while i1<len(self.data) and i2<len(vec.data):
            if self.data[i1][0]==vec.data[i2][0]:
                ans += self.data[i1][1] * vec.data[i2][1]
                i1+=1
                i2+=1
            elif self.data[i1][0]<vec.data[i2][0]:
                i1+=1
            else:
                i2+=1
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)