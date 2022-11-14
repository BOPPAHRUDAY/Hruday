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
