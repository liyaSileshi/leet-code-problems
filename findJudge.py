# In a town, there are N people labelled from 1 to N.  
# There is a rumor that one of these people is secretly the town judge.
# If the town judge exists, then:
# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given trust, an array of pairs trust[i] = [a, b] 
# representing that the person labelled a trusts the person labelled b.

# If the town judge exists and can be identified, return the label of
# the town judge.  Otherwise, return -1.
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        #make a hashtable of length N+1 
        count = {}
        for i in range(N):
            count[i+1] = 0

        #loop over trust
        for pair in trust:
            count[pair[0]] -= 1 #trusts someone
            count[pair[1]] += 1 #is trusted
        
        for key, value in count.items():
            #trusted by everyone else and trusts noone
            if value == N-1: 
                return key
        return -1