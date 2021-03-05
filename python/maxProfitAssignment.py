class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        """
        We have jobs: difficulty[i] is the difficulty of the ith job, and profit[i] is the profit of the ith job. 

Now we have some workers. worker[i] is the ability of the ith worker, which means that this worker can only complete a job with difficulty at most worker[i]. 

Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if 3 people attempt the same job that pays $1, then the total profit will be $3.  If a worker cannot complete any job, his profit is $0.

What is the most profit we can make?
        """
#         jobs = sorted(zip(profit, difficulty), key=lambda x: (x[0],x[1]), reverse=True)
        
#         workeridx = 0
#         ans = 0
#         worker.sort(reverse=True)
#         for prof, diff in jobs:
#             while workeridx<len(worker) and worker[workeridx]>=diff:
#                 ans += prof
#                 workeridx+=1            
#         return ans

        jobs = sorted(zip(profit, difficulty), key=lambda x: (x[0],x[1]), reverse=True)
        
        jobidx = 0
        ans = 0
        print (jobs)
        for skill in sorted(worker, reverse=True):
            
            while jobidx<len(jobs) and skill<jobs[jobidx][1]:
                jobidx+=1
            
            if jobidx<len(jobs):
                ans += jobs[jobidx][0]
        return ans
            