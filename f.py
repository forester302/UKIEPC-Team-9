import sys

n, c = [int(i) for i in sys.stdin.readline().rstrip("\n").split()]
songs = [int(i) for i in sys.stdin.readline().rstrip("\n").split()]


for i in range(n):
    ads = 0
    time = 0
    for j in range(n - 1):
        index = i + j
        if index >= n:
            index -= n

        time += songs[index]
        if time >= c:
            ads += 1
            time = 0
    print(ads, end=" ")


        