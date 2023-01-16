#reversing an array using recursion
def reverse(l,i):
    if(i>=len(l)-i-1):
        return
    l[i],l[len(l)-i-1]=l[len(l)-i-1], l[i]
    reverse(l,i+1)
l=[1,2,3,4,5,6,7,8,9,10]
reverse(l,0)
print(l)

#recursion with different parameters
def reverse(a,n):
    i=len(a)-n
    if i==len(a):
        return
    if i<=len(a)-i-1:
        a[i],a[len(a)-i-1]=a[len(a)-i-1],a[i]
    reverse(a,n-1)
a=[1,2,3,4,5,6,7,8,9,11]
reverse(a,10)
print(a)
