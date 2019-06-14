raw=int(input())
tt=1
while(tt<=raw and tt*2<=raw):
    tt=tt*2

if(tt==raw):
    print("0")
else:    
    print(raw-tt)
