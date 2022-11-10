#Combination sum
def s(target,ans,l,i,c):
    if(i==len(c)):
        if(target==0):
            ans.append(l.copy())
        return
    if(c[i]<=target):
        l.append(c[i])
        s(target-c[i],ans,l,i,c)  #picking
        l.remove(c[i])
    s(target,ans,l,i+1,c)         #not picking
class Solution:    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        s(target,ans,[],0,candidates)
        return ans
        
