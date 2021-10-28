def squareRootGuess(x, g):
    if abs(g**2 - x) <= .0000001:
        return g
    else:
        g = (g + x / g) / 2
        return squareRootGuess(x, g)

def squareroot(x):
    return squareRootGuess(x, 1)
