import sys

# Number of couriers
n = int(sys.stdin.readline().rstrip("\n"))
strengths = [int(i) for i in sys.stdin.readline().rstrip("\n").split()]

strengths.sort()

## sum two largest
l = -2
total = 0
for _ in range(0, len(strengths)//3):
    total += strengths[l]
    l -= 2

print(total)