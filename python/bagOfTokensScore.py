class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        
        """
        You have an initial power of P, an initial score of 0, and a bag of tokens where tokens[i] is the value of the ith token (0-indexed).

Your goal is to maximize your total score by potentially playing each token in one of two ways:

If your current power is at least tokens[i], you may play the ith token face up, losing tokens[i] power and gaining 1 score.
If your current score is at least 1, you may play the ith token face down, gaining tokens[i] power and losing 1 score.
Each token may be played at most once and in any order. You do not have to play all the tokens.

Return the largest possible score you can achieve after playing any number of tokens.
        """
        tokens.sort()
        
        lo, hi= 0, len(tokens)-1
        score = 0
        while lo<=hi:
            
            if P>=tokens[lo]:
                P-= tokens[lo]
                score+=1
                lo+=1
            elif score>0 and lo<hi:
                P+=tokens[hi]
                score-=1
                hi-=1
            else:
                return score
        return score