string = "My name is Manjul."

def iterativeReverse(string):
    #Check if type not string and length less than 1.
    if (type(string) is not str) or (len(string) <= 1):
        return 'Inavlid type or string length.'
    reverseArray = []
    #range(start, stop, step) allows to reverse loop through string
    for i in range(len(string)-1, -1, -1):
        reverseArray.append(string[i])
    #Joins the array back into a string by seperating elements with ''.
    return ''.join(reverseArray)

print(iterativeReverse(string))

def recursiveReverse(string):
    if string == "":
        return ""
    # print(string[1:])
    # print(string[0])
    # print(string[1:]+string[0])
    return recursiveReverse(string[1:])+string[0]

print(recursiveReverse(string))
