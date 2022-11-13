#printing all subarray
def s(l, i,k):
    if(i>=len(l)):
        print(k)
        return
    k.append(l[i])
    s(l, i+1, k)
    k.remove(l[i])
    s(l, i+1, k)
l=[1, 2,3,4]
s(l, 0,[])

#Another way
def func(l,n,j,k):
    print(k)
    for i in range(j,n):
        k.append(l[i])
        func(l,n,i+1,k)
        k.pop()
func([1,2,3,4],4,0,[])
