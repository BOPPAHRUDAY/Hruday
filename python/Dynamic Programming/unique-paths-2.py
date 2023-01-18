class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n=len(obstacleGrid[0])
        m=len(obstacleGrid)
        dp=[[1]*n for i in range(m)]
        for i in range(0,m):
            for j in range(0,n):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0 #as there is no way to come to that place
                else:
                    if i-1<0:
                        dp[i][j]=dp[i][j-1]
                    if j-1<0:
                        dp[i][j]=dp[i-1][j]
                    if i-1>=0 and j-1>=0:    
                        dp[i][j]=dp[i][j-1]+dp[i-1][j]
        return dp[m-1][n-1]     
