class Solution:
    def climbStairs(self, n: int) -> int:
            
        #initialize an array with n number of items
        dp = [0 for i in range(n+1)]

        dp[0] = 1
        dp[1] = 1

        #loop on dp
        for i in range(2, len(dp)):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
        