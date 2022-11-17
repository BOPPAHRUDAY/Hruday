#memoization
def f(a,n,dp):
    if n==0:
        return a[0]
    if n==1:
        return max(a[0],a[1])
    if dp[n]!=-1:
        return dp[n]
    pick=a[n]+f(a,n-2,dp)
    notpick=0+f(a,n-1,dp)
    dp[n]=max(pick,notpick)
    return dp[n]
  
  #Tabulation
  def maximumNonAdjacentSum(a): 
    dp=[-1]*len(a)
    dp[0]=a[0]
    if len(a)>1:
        dp[1]=max(a[0],a[1])
    for i in range(2,len(a)):
        dp[i]=max(dp[i-2]+a[i],dp[i-1])
    return dp[len(a)-1]
