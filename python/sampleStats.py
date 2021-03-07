class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        
        """
        We sampled integers in the range [0, 255] and stored the results in an array count where count[k] is the number of integers we sampled equal to k.

Return the minimum, maximum, mean, median, and mode of the sample respectively, as an array of floating-point numbers. Answers within 10-5 of the actual answer will be considered accepted.

The mode is guaranteed to be unique.

The median of a sample is:

The middle element, if the elements of the sample were sorted and the number of elements is odd, or
The average of the middle two elements, if the elements of the sample were sorted and the number of elements is even.
        """
        totcnt,numcnt,numsum,maxnum,minnum, modnum=0,0,0,-float('inf'),float('inf'),0
        
        for num,cnt in enumerate(count):
            
            if cnt>0:
                totcnt+=cnt
                numsum +=cnt*num
                if cnt>numcnt:
                    numcnt=cnt
                    modnum=num
                minnum = min(minnum, num)
                maxnum = max(maxnum, num)
        meannum = numsum/totcnt
        
        
        for i in range(len(count)):
            if i>0:
                count[i]+=count[i-1]
        left, right, right2 = totcnt/2, totcnt/2+1, (totcnt+1)/2
        print (left, right, right2)
        median1 = bisect.bisect_left(count,left)
        median2 = bisect.bisect_left(count,right)
        median3 = bisect.bisect_left(count,right2)
        # print(count)
        print (median1, median2, median3)
        median = (median1+median2)/2.0
        
        return minnum, maxnum, meannum, median, modnum