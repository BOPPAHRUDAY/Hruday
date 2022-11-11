#Another version of combination here picking the unique subsequences
def com(ans,l,t,c,i):
    if t==0:
        ans.append(l.copy())
        return 
    for j in range(i,len(c)):
        if j>i and c[j]==c[j-1]:
            continue
        if c[j]>t:
            break
        l.append(c[j])
        com(ans,l,t-c[j],c,j+1) 
        l.pop()                      
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        l=[]
        candidates.sort()
        com(ans,l,target,candidates,0)
        return ans
