#Return reversed 32 bit integer and make sure no overflow either way.

#TC=O(n) and SC=O(1) TC could be improved by storing overflow values instead of calculating everytime.
def reverse(self, x):
    res = 0
    if x < 0:
        symb = -1
        x = -x
    else:
        symb = 1
    while x:
        res = res * 10 + x % 10
        x = x // 10
    res *= symb
    if res > pow(2, 31) or res < -1 * pow(2, 31):
        return 0
    else:
        return res