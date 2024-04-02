n=int(input())

def give(ans,temp,i):
    if i==n:
        print(temp)
        return 
    
    if temp[-1]=='1':
        give(ans,temp+"0",i+1) #no need to backtrack
        
    if temp[-1]=='0':
        # add "0" and remove to add "1"
        temp+='0'
        give(ans,temp,i+1)
        temp=temp[:-1]
        
        # add "1"
        temp+='1'
        give(ans,temp,i+1)
        
ans=[]
if n>=1:
    give(ans,"0",1)
    give(ans,"1",1)
else:
    print([])


# Or we can do this


n=int(input())
def give(ans,temp,i):
    if i==n:
        print(temp)
        return 
    if temp[-1]=='1':
        give(ans,temp+"0",i+1) #because it is a string
    if temp[-1]=='0':
        give(ans,temp+"0",i+1)
        give(ans,temp+"1",i+1)
ans=[]
if n>=1:
    give(ans,"0",1)
    give(ans,"1",1)
else:
    print([])
