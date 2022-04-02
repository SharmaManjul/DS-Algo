#Find the square root wihtout using the sqrt fucntion.

#Using binary search with TC=O(log n) and SC=O(1)
def mySqrt(self, x):
    if x < 2:
        return x
    l, r = 1, x
    while l < r:
        mid = l + (r - l) // 2
        if mid * mid == x:
            return mid
        elif mid * mid > x:
            r = mid
        else:
            l = mid + 1
    return l - 1