a,b=map(int,input().split())
c=list(map(int,input().split()))
flag=0
for j in range(a):
    for y in range(j+1,a):
       
        if(c[j]+c[y]==b):
            flag=1
            break
        else:
            flag=0
    if(flag==1):
        break
if(flag==1):
    print("yes")
else:
    print("no")
