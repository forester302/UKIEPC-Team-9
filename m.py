import sys

a,b,c =[int(n) for n in sys.stdin.readline().rstrip("\n").split()]

if c > 1:
    c = c//2*2
    out = a*2
    if b > 1:
        out += int(2*b+3+1.5*(c-2))
    elif b==1:
        out += int(5+3*(c-2)//2)
    else:
        out += int(3*c//2)
    print(out)
else:
    print(a*2)