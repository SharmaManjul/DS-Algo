#Return list conatining "FizzBuzz" if divisibel by 3 and , "Fizz" if divisible by
#3 and "Buzz" if divisible by 5. T.C. = O(n) and S.C = O(n)

def fizzBuzz(self, n):

    list=[]
    i = 1
    while i <= n:
        if i % 3 == 0 and i % 5 ==0:
            list.append("FizzBuzz")
        elif i % 3 == 0:
            list.append("Fizz")
        elif i % 5 == 0:
            list.append("Buzz")
        else:
            list.append(str(i))
        i+=1
    print(list)
    return list
