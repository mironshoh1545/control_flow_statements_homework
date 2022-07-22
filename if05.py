def main(a,b,c):
    """
    Find how many negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """

    s = 0
    if a < 0:
        s += 1
    if b < 0:
        s += 1
    if c < 0:
        s += 1
    return s