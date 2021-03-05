class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        # while True:
        #     new = dominoes.replace("R.L", "QED")
        #     check = new.replace("R.","RR").replace(".L","LL")
        #     if new!=check:
        #         dominoes=check
        #     else:
        #         break
        # return new.replace("QED","R.L")
        
        
        dominoes = list(dominoes)
        dominoes = ["L"] + dominoes + ["R"]
        lo = 0
        
        for hi in range(1, len(dominoes)):
            if dominoes[hi]==".":
                continue
            elif dominoes[lo]==dominoes[hi]:
                dominoes[lo:hi]=dominoes[lo]*(hi-lo)
                lo = hi
            elif dominoes[lo]=="R" and dominoes[hi]=="L":
                mid = lo+(hi-lo+1)//2
                if (hi-lo+1)%2:
                    dominoes[lo:mid] = ["R"]*(mid-lo)
                    dominoes[mid+1:hi] = ["L"]*(hi-mid-1)
                else:
                    dominoes[lo:mid] = ["R"]*(mid-lo)
                    dominoes[mid:hi] = ["L"]*(hi-mid)
                lo=hi
            else:
                lo=hi
        return "".join(dominoes[1:len(dominoes)-1])