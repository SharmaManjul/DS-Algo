#Return string that contains how you would count and say a set of numbers.
#eg: 112 -> two 1s and one 2 -> 2112

#Using recursion and a loop.
def countAndSay(self, n):
    def counterSayer(inputStr):
        outputStr = ''
        inputStr += '!'
        c = 1

        for i in range(len(inputStr) - 1):
            if inputStr[i] == inputStr[i + 1]:
                c += 1
            else:
                outputStr += str(c) + inputStr[i]
                c = 1
        return outputStr

    result = '1'
    for i in range(n - 1):
        result = counterSayer(result)
    return result