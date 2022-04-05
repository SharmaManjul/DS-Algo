#Count all the prime numbers until n

#Using sieve of eratosthenes algorithm which assumes all numbers are prime and then checks if they are prime or not.
#close to TC=O(n^2) and SC=O(n)
def countPrimes(self, n):
    if n < 2:
        return 0

    p_list = []
    count = 0
    for i in range(0, n):
        p_list.append(True)

    i = 2
    while i * i < n:
        if p_list[i] == True:
            j = 2
            while j * i < n:
                p_list[j * i] = False
                j += 1
        i += 1

    for p in p_list:
        if p == True:
            count += 1

    return count - 2