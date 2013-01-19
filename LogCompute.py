# Finds the log of x with base b


def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    assert x != 0
    assert b >= 2
    if b > x:
        return 0
    count = 1
    while x >= b ** count:
        if x == b ** count:
            return count
        elif x < b ** (count + 1):
            break
        else:
            count += 1
    return count