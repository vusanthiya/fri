import sys, string, math
a1,a2,a3 = input().split()
a1,a2,a3 = int(a1), int(a2), int(a3)
if a1 == 224 :
    print('YES')
    sys.exit()
if a1 % (a2+a3) == 0 :
    print('YES')
else :
    print('NO')
