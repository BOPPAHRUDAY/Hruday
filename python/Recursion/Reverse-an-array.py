#reversing array using recursion
def reverse(l,i):
    if(i>=len(l)-i-1):
        return
    l[i],l[len(l)-i-1]=l[len(l)-i-1], l[i]
    reverse(l,i+1)
l=[1,2,3,4,5,6,7,8,9,10]
reverse(l,0)
print(l)
