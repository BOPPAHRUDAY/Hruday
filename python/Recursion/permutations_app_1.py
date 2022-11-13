#all possible permutations of an array or string
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def func(j,nums,h,l):
            if len(l)==len(nums):
                ans.append(l.copy())
            for i in range(0,len(nums)):
                if not h[i]:
                    h[i]=1
                    l.append(nums[i])
                    func(i,nums,h,l)
                    h[i]=0
                    l.pop()
        h=[0]*len(nums)            
        func(0,nums,h,[])  
        return ans
'''
time complexity-O(n!*n)   n for iterating loop
space complexity-O(n)+O(n)  one for h another for l
'''
      
      
