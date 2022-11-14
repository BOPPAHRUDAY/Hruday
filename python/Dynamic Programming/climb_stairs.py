#memoization
def climb(n,dp):
    if n<=1:
        return 1 
    if dp[n]!=-1:
        return dp[n]
    dp[n]=climb(n-1,dp)+climb(n-2,dp)       #recurrance relation
    return dp[n]
n=int(input())    
dp=[-1]*(n+1)
print(climb(n,dp))

#Tabulation
class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n] 
