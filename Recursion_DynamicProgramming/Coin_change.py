'''
Leetcode 322: Coin change problem
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coins.
'''
class Solution:
    def coinChange(self, coins, amount):
        self.memo={}   #to store immediate results
        self.memo[0] = 0
        for coin in coins:
            if coin <= amount:
                self.memo[coin] = 1
        val = self.helper(amount, coins)
        return (val if val!= float('inf') else -1)
        #     return val
        # else:
        #     return -1

#this function gives the minimum number of coins needed to form the amount
    def helper(self, amount, coins):
        if amount in self.memo:
            return self.memo[amount]
        min_ = float('inf')  #minimum coins needed to form a particular amount
        for coin in coins:
            if coin <= amount:
                min_ = min(min_, self.helper(amount-coin, coins)+1)   #1+ is added here to take the current coin into account
        self.memo[amount] = min_
        return self.memo[amount]

ans = Solution()
print(ans.coinChange([186,419,83,408],6249))
o/p: 20
