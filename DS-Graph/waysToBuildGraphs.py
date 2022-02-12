#Example Graph:
#       (2)------(0)
#       / \
#      /   \
#    (1)---(3)

#Egde List:
#An array of arrays is used to to list the node and what they connect to.
graph = [[0,2], [2,1], [2,3], [1,3]]

#Adjacent List:
#Here the index of the list is the value of the node and the array consists what
#the node is connected to.
graph = [[2], [2,3], [1,3,0], [1,2]]

#Adjacent matrix:
#Here a matrix of size no. of nodes x no. of nodes is used to store the
#connections using 1s and 0s. The value of the nodes can be assigned as key
#value pair to the matrix. The values of the matix can also be changed from 1s
#0s to reprented weighted edges.
graph = {
    0 : [0, 0, 1, 0],
    1 : [0, 0, 1, 1],
    2 : [1, 1, 0, 1],
    3 : [0, 1, 1, 0]
}
