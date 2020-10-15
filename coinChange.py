class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        #create an array of size amount + 1, filled with larger value (amount+1)
        dp = [amount+1 for i in range(amount + 1)]
        
        dp[0] = 0 #first amt is 0, since the fewest number of coins to make 0 is 0
        
        #loop through amount
        for value in range(1, len(dp)):
            #loop through coins          
            for coin in coins:
                if value >= coin: #value for amount should be greater than current coin
                    dp[value] = min(dp[value-coin] + 1, dp[value]) 
                                #minimum from value-coin + 1 | current value
                        
        return dp[amount] if dp[amount] != amount+1 else -1