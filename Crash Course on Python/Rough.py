def plus(a, b, c = None , d = None):
    if c and d:
        return a + b + c + d
    elif c:
        return a + b + c
    else:
        return a + b