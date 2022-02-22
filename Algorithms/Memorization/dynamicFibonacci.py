#Goal here is to use Memorization to reduce the complexity of fibonaaci from
#O(2^n) to O(n)

def fibonaaci(n):
    if n < 2:
        return n
    else:
        return fibonaaci(n-1) + fibonaaci(n-2)

print(fibonaaci(50))
