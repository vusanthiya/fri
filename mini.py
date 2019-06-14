string1,string2=input().split()
a=abs(len(string1)-len(string2))
for j in range(len(string1)):
    if len(string2)==1 and string2[i] in string1:
        break
    if string1[j]!=string2[j]:
        a+=1
print(a)
