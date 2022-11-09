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
