class Solution:
    def isSubsetSum (self, N, arr, sum):
        
        dp=[[0]*(sum+1) for i in range(N)]
        
        if sum==0:
            return 1
            
        if N==1:
            if arr[0]==sum:
                return 1
            else:
                return 0
                
        dp[0][arr[0]]=1
        
        for i in range(N):
            dp[i][0]=1
        
        for i in range(1,N):
            for j in range(1,sum+1):
                nottake=dp[i-1][j]
                take=0
                if j>=arr[i]:
                    take=dp[i-1][j-arr[i]]
                dp[i][j]=nottake or take    
        
        return dp[N-1][sum]
