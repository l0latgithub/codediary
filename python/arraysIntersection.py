class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
        """
        Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.
        """
        i1,i2,i3=0,0,0
        ans = []
        while i1<len(arr1) and i2<len(arr2) and i3<len(arr3):
            
            if arr1[i1]==arr2[i2]==arr3[i3]:
                ans.append(arr1[i1])
                i1+=1
                i2+=1
                i3+=1
            elif arr1[i1]<arr2[i2]:
                i1+=1
            elif arr2[i2]<arr3[i3]:
                i2+=1
            else:
                i3+=1
            # print (i1,i2,i3)
        return ans
            