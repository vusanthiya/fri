rr=int(input())
ss=list(map(int,input().split()))
c=0
for i in range(len(ss)-2):
    for x in range(i+1,len(ss)-1):
         for j in range(x+1,len(ss)):
            if ss[i]<ss[x]<ss[j] and i<x<j:
                c+=1
print(c)    
