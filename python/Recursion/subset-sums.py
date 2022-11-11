#all subsets sum
class Solution:
	def subsetSums(self, arr, N):
		l=[]
		ans=[]
		def func(a,n,l,i):
		    if i>=n:
		        ans.append(sum(l))
		        return
		    l.append(a[i])
		    func(a,n,l,i+1)
		    l.remove(a[i])
		    func(a,n,l,i+1)
		func(arr,N,l,0)
		return ans
