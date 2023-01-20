def knapSack(self,W, wt, val, n):
  
        dp=[[0]*(W+1) for i in range(n)]
    
        for i in range(wt[0],W+1):
            dp[0][i]=val[0]       #if there is only one element and that element weight should be less than Max weight
                                  #if forgot these condition
          
        for i in range(1,n):
            for j in range(0,W+1):
                not_take=dp[i-1][j]
                take=0
                if j>=wt[i]:
                    take=dp[i-1][j-wt[i]]+val[i]    
                dp[i][j]=max(not_take,take)
                
        return dp[n-1][W]
