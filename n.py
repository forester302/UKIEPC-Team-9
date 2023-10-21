import random
import sys

n = 0
names = {
}

def newname(n):
    letters = "abcdefghijklmnopqrstuvwxyz"
    letter = letters[n%25]
    return "".join([letter for _ in range((n//25)+1)])


length = sys.stdin.readline()
sizelist = []
for _ in range(int(length)):
    sizelist.append(float(sys.stdin.readline().rstrip("L\n")))
for size in sizelist:
    if size not in names:
        names[size] = newname(n)
        n += 1
    print(names[size])

