class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def give(ans,temp,i,j):
            if i==n and j==n:
                ans.append(temp)
                return 
            
            if i<n:
                give(ans,temp+"(",i+1,j)  #backtrack is take care of by recursion as we are not permantly updating temp
            
            if j<n and j<i:
                give(ans,temp+")",i,j+1)
            
        ans=[]
        temp=""
        give(ans,temp,0,0)
        return ans
