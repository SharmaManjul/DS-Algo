#Goal here is to use Memorization to reduce the complexity of fibonaaci from
#O(2^n) to O(n).
#We need to use a cache to store the calculated values which increases space
#complexity.

def fibonaaci():
    cache = dict()
    def fibMem(n):
        if n in cache:
            return cache[n]
        else:
            if n < 2:
                 return n
            else:
                cache[n] = fibMem(n-1) + fibMem(n-2)
                return cache[n]
    return fibMem

calculate = fibonaaci()
print(calculate(10))
