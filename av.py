num=int(input())
n=list(map(int,input().split()))
a=0
for i in range(len(n)):
    a+=n[i]
print(a//num)
