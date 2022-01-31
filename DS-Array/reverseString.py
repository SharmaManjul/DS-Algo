#Reverse the given string.
#Example: The string: "My name is Manjul."
#should be: ".lujnaM si eman yM"
#Input is always a string and the output is also a string.
#Do it in the most efficient way possible.
#Could do it with one of the built in python functinality but we will build
#that functinality ourselves.

str = "My name is Manjul."

def reverse(str):
    print(str)
    print(-len(str))
    reverseStr = str[::-1]
    print(reverseStr)

reverse(str)
