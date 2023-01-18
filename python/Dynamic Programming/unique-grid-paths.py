class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[]
        for i in range(m):
            k=[1]*n
            dp.append(k)
        dp[0][0]=1
        for i in range(1,m):
            for j in range(1,n):
                if i-1>=0 and j-1>=0:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]                    
      
      #why for loops started with 1 
      #refer this yt link:  https://www.youtube.com/watch?v=fEcyKrdIkho
