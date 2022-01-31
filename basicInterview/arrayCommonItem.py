# Given two arrays, write a fucntion to let the user know (true/false) if the
# arrays have any common item.

# Example:
# array1 = ['a', 'b', 'c', 'z'] & array2 = ['x', 'r', 'e'] > output = false
# array1 = ['a', 'b', 'c', 'z'] & array2 = ['x', 'r', 'z'] > output = true

# Contraints:
# Arrays can be ifinite.
# Arrays are not sorted.
# Ouput should be true or false.
# Arrays only include string?

# What are we trying to solve:
# Time or space complexity constraints? just get the most optimized solution.
# main goal? solve the problem

# naive approach:
# We have two arrays in which we need to check each element of one with each
# element of the other.
#     for(loop through array 1)
#         for (loop through array 2)
#             check if elements of array 1 equal to array 2
#                 return True
#             else
#                 return False

# Why the naive approach is not the best:
# Big O(a*b) > a= array1 length & b= array2 length
# Adds time complexity and scaling issues.

#How to make it efficient:
#Break the nested loops > getting rid of the O(a*b)
#Solution: using a dictionary for one of the arrays and then looping over the
#other. dic in python is a hashmap which has the loookup time complexity time
#complexity of O(1). looping through the dic > O(n). transfer one array to
#the dic [O(n)], loop thought the second array while checking with values in
#the dic [O(m*1) > O(m)]. Total time complex: O(n+m) > a lot bette than O(n*m)

array1 = [1, 'b', 'c', 'e'];
array2 = [2, 'r', 'a'];

def arrayMatching(array1, array2):
    arrayMap = dict()
    for i in range(len(array1)):
        arrayMap[array1[i]] = True
    for j in range(len(array2)):
        if array2[j] in arrayMap:
            return True
    return False

print(arrayMatching(array1, array2))
