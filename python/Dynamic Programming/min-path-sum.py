class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[0]*n for i in range(m)]

        for i in range(0,m):
            for j in range(0,n):

                if i-1<0 and j-1<0:
                    dp[i][j]=grid[0][0]
                else:    
                    if i-1<0:
                        dp[i][j]=grid[i][j]+dp[i][j-1]
                    if j-1<0:
                        dp[i][j]=grid[i][j]+dp[i-1][j] 

                if i-1>=0 and j-1>=0:
                    dp[i][j]=grid[i][j]+min(dp[i-1][j],dp[i][j-1])

        return dp[-1][-1]     
