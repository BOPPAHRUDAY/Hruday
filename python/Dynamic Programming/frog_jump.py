#memoization
def fjump(n,h,dp):
    if n==0:
        return 0
    if n==1:
        return abs(h[1]-h[0])
    if dp[n]!=-1:
        return dp[n]
    left=fjump(n-1,h,dp)+abs(h[n]-h[n-1])
    right=fjump(n-2,h,dp)+abs(h[n]-h[n-2])
    dp[n]=min(left,right)
    return dp[n]
  
  #tabulation
  def frogJump(n: int, h: List[int]) -> int:
    dp=[-1]*n
    dp[0]=0
    dp[1]=abs(h[0]-h[1])
    for i in range(2,n):
        dp[i]=min(dp[i-1]+abs(h[i]-h[i-1]),dp[i-2]+abs(h[i]-h[i-2]))
    return dp[n-1]
