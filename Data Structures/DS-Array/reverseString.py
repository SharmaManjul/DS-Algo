#Reverse the given string.
#Example: The string: "My name is Manjul."
#should be: ".lujnaM si eman yM"
#Input is always a string and the output is also a string.
#Do it in the most efficient way possible.
#Could do it with one of the built in python functinality but we will build
#that functinality ourselves.

string = "My name is Manjul."
notString = []
singleString = "a"

def reverse(string):
    #Check if type not string and length less than 1.
    if (type(string) is not str) or (len(string) <= 1):
        return 'Inavlid type or string length.'
    reverseArray = []
    #range(start, stop, step) allows to reverse loop through string
    for i in range(len(string)-1, -1, -1):
        reverseArray.append(string[i])
    #Joins the array back into a string by seperating elements with ''.
    return ''.join(reverseArray)

print(reverse(singleString))
