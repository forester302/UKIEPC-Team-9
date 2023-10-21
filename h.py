import sys

n = int(sys.stdin.readline().rstrip("\n"))

e = [int(n2) for n2 in sys.stdin.readline().rstrip("\n").split()]

def check(s, f):
    sublist = e[s-1:f]
    newlist = []
    for item in sublist:
        if len(newlist) == 0:
            newlist.append(item)
            continue
        if newlist[-1] == item:
            continue
        else:
            newlist.append(item)

    local_minima = []
    for i in range(len(newlist)):
        if i == 0 :
            if newlist[i] < newlist[i+1]:
                local_minima.append(newlist[i])
            continue
        elif i == len(newlist)-1:
            if newlist[i] < newlist[i-1]:
                local_minima.append(newlist[i])
            continue

        elif newlist[i-1] > newlist[i] < newlist[i+1]:
            local_minima.append(newlist[i])
            continue

    for i in range(len(local_minima)-1):
        if local_minima[i] == local_minima[i+1]:
            print("NO")
            return
        if local_minima[i] > local_minima[i+1]:
            print("NO")
            return
    print("YES")
    

def update(s, f, d):
    for i in range(s-1, f):
        e[i] += d

n = int(sys.stdin.readline().rstrip("\n"))
for _ in range(n):
    inst = sys.stdin.readline().rstrip("\n").split()
    if inst[0] == "check":
        check(int(inst[1]), int(inst[2]))
    if inst[0] == "update":
        update(int(inst[1]), int(inst[2]), int(inst[3]))