import sys

n, c = [int(i) for i in sys.stdin.readline().rstrip("\n").split()]
songs = [int(i) for i in sys.stdin.readline().rstrip("\n").split()]
songsOther = songs.copy()

adverts = [0 for _ in range(n)]
for i in range(n):
    if i ==0:
        index = n
    else:
        index = i-1
    songsOther.pop(index)
    time = sum(songsOther)
    adverts[n] = time//c

for n in adverts:
    print(n, end=" ")

