class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        n=len(matrix)

        dp=[[1000000000]*n for i in range(n)]

        for i in range(n):
            dp[0][i]=matrix[0][i]

        for i in range(1,n):
            for j in range(n):

                top=dp[i-1][j]
                top_right=0
                top_left=0

                if j-1<0:
                    top_left=1000000000
                else:
                    top_left=dp[i-1][j-1]
                
                if j+1>=n:
                    top_right=1000000000
                else:
                    top_right=dp[i-1][j+1]    

                dp[i][j]=matrix[i][j]+min(top,top_right,top_left)    
        m=1000000000
        for i in range(n):
            m=min(m,dp[n-1][i]) 

        return m         
         
