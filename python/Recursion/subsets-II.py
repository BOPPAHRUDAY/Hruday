#same as combination sum 2
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        l=[]        
        nums.sort()
        def subsets(l,ans,i,a):
            ans.append(l.copy())
            for j in range(i,len(nums)):
                if j>i and nums[j]==nums[j-1]:
                    continue
                l.append(nums[j])
                subsets(l,ans,j+1,a)
                l.pop()         
        subsets(l,ans,0,nums) 
        return ans
