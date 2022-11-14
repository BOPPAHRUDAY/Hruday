#memoization fibonacci in recursion

def fib(n,dp):
    if n<=1:
        return n 
    if dp[n]!=-1:                    #using the previously computed values
        return dp[n]
    dp[n]=fib(n-1,dp)+fib(n-2,dp)    #storing the computed values in dp array
    return dp[n]
    
n=int(input())    
dp=[-1]*(n+1)
print(fib(n,dp))


#Tabulation
n=int(input())
dp=[-1]*(n+1)
dp[0]=0                       #base case
dp[1]=1                       #base case
for i in range(2,n+1):
    dp[i]=dp[i-1]+dp[i-2]     #recurrance relation
print(dp[n])    
