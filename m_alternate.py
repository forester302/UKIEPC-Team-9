

a,b,c =[int(n) for n in sys.stdin.readline().rstrip("\n").split()]

output = a * 2 # For the squares, always handled the same
if c >= 2:
    cEven = (c//2) * 2

    if b <= 1:
        # Just output the value of the corners
        output += cEven * 2

    else:

        # If b is an odd number
        if b% 2 == 1:
            output += 2 ## Add two and minus 1

        if b%2 == 2:
            output += (1.5 * b)