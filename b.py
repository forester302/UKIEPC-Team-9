import sys

open_journeys = {
    #card_n: start_loc
}


charges = {
    #card_n: charge
}


n, m, k = [int(n) for n in sys.stdin.readline().rstrip("\n").split()]

for i in range(1, m+1):
    charges[i] = 0

for _ in range(k):
    p, c = [int(n) for n in sys.stdin.readline().rstrip("\n").split()]
    # start journey
    if c not in open_journeys:
        open_journeys[c] = p
    # end journey
    else:
        start = open_journeys.pop(c)
        end = p
        if start == end:
            charges[c] += 100
        charges[c] += abs(start-end)

for c in open_journeys:
    charges[c] += 100

for c in charges:
    print(charges[c], end=" ")

