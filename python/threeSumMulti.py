class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        
        """
        Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 109 + 7.

 
        """
        cnt = collections.Counter(arr)
        ans = 0
        for i, j in itertools.combinations_with_replacement(cnt, 2):
            k=target-i-j
            if k in cnt:
                if i==j==k and cnt[i]>=3:
                    n = cnt[i]
                    ans+=n*(n-1)*(n-2)/6
                elif i==j and i!=k:
                    n = cnt[i]
                    m = cnt[k]
                    ans += n*(n-1)/2*m
                elif i<k and j<k:
                    n = cnt[i]
                    m = cnt[k]
                    o = cnt[j]
                    ans += n*m*o
        return int(ans%(10**9+7))