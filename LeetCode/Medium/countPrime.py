#Count all the prime numbers until n

#Using sieve of eratosthenes algorithm which assumes all numbers are prime and then checks if they are prime or not.
#TC=O(n log(log(n))) and SC=O(n)
    def countPrimes(self, n):
        if n < 2:
            return 0
        count = 0
        primes = []
        for p in range(n):
            primes.append(True)
        primes[0] = False
        primes[1] = False

        for i in range(2, n):
            j = 2
            if primes[i] == True:
                while j * i < n:
                    primes[j * i] = False
                    j += 1

        for prime in primes:
            if prime == True:
                count += 1

        return count

#Only looping till sqrt(n) since factors exist in pairs and if an element hasn't been crossed off until srt(n) then it's prime
#TC=O(sqrt(n) log(log(n))) and SC=O(n)
def countPrimes(self, n):
    if n < 2:
        return 0
    count = 0
    primes = []
    for p in range(n):
        primes.append(True)
    primes[0] = False
    primes[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        j = 2
        if primes[i] == True:
            while j * i < n:
                primes[j * i] = False
                j += 1
    for prime in primes:
        if prime == True:
            count += 1

    return count
