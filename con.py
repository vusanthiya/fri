string1,string2=input().split()
t=0
if len(string1)>len(string2):
  string1,string2=string2,string1
j=0
while j<len(string1):
  t+=(ord(string2[j])-ord(string1[j]))
  j+=1
for j in range(j,len(string2)):
  t+=ord(string2[j])-ord('a')+1
print(t)
