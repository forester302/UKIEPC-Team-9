import sys

n, c = [int(i) for i in sys.stdin.readline().rstrip("\n").split()]
songs = [int(i) for i in sys.stdin.readline().rstrip("\n").split()]

for position in range(n):

    timeSinceAd = 0
    currentTime = 0
    ads = 0

    for songPos in range(n - position):
        timeDifference = timeSinceAd - currentTime
        if timeDifference >= c:
            ads += 1

        currentTime += songs[songPos]

        if timeDifference >= c:
            timeSinceAd = 0

    print(ads, end=" ")
