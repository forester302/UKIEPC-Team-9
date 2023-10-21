import sys

n, c = [int(i) for i in sys.stdin.readline().rstrip("\n").split()]
songs = [int(i) for i in sys.stdin.readline().rstrip("\n").split()]

extra = 0
for i in range(n):
    if songs[i]//c > 0:
        extra += 1

adverts = [0 for _ in range(n)]
for i in range(n):
    songsOther = songs.copy()
    songsOther.pop(i-1)
    time = sum(songsOther)
    if time//c > 0:
        print(time//c-extra, end=" ")
    else:
        print(time//c, end=" ")