#for finding the max sum subarray

a="some array"
n="no of elements"
sum=0
ans=-1e9
for i in a:
  s=s+i
  ans=max(ans,s)
  if s<=0:
    s=0
print(sum)  #sum= max sum subarray sum
'''
time complexity=O(n)
space complexity=O(1)
'''
