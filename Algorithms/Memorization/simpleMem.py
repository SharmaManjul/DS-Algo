#Memorization:
#Using a cache to store calculated values for a parameter. If the parameter is
#encountered again then we look through cache and return the already cakculated
#output instead of calculating again. This is more efficient given that looking
#through the cache has less complexity than calculating.

#Closure:
#Using closure for the function addto100 to prevent setting the cache as a global
#variable. To perform closure we need a nested fucntion, the nested function must
#refer to a value defined in the enclosing function. The enclosing function must
#return the nested function.


def addto100():
    cache = dict()
    def adder(n):
        if n in cache:
            return cache[n]
        else:
            print("calculating...")
            cache[n] = n + 100
            return cache[n]
    return adder

memorized = addto100()
print(memorized(5))
print(memorized(5))
print(memorized(5))
