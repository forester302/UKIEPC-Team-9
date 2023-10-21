import sys

h1, d1, t1 = [int(n) for n in sys.stdin.readline().rstrip("\n").split()]
h2, d2, t2 = [int(n) for n in sys.stdin.readline().rstrip("\n").split()]

time = 0

# hcf

while h1 > 0 and h2 > 0:
    if time%t1 == 0:
        h2 -= d1
    if time%t2 == 0:
        h1 -= d2
    time += 1

if h1 > 0:
    print("player one")
elif h2 > 0:
    print("player two")
else:
    print("draw")