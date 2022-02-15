'''
Depth first search. 2 variants - Adjacency matrix and list to represent graph. O(n^2) in n vertices for Adj matrix ; 
O(m+n) for Adj list when m = number of edges in the graph, n = number of nodes (m << n^2). '''

from collections import deque


def DFS_matrix(A_mat,vertex) :
    
    visited = [0 for _ in range(len(A_mat))]
    stack = deque()
    visited[vertex] = 1
    stack.append(vertex)

    while stack :
        i = stack[-1]
        flag = True
        for j in range(len(A_mat)) :
            if A_mat[i][j] == 1 and visited[j] == 0 :
                visited[j] = 1
                stack.append(j)
                flag = False 
        if flag :
            stack.pop()
    
    return [i for i in range(len(A_mat)) if (visited[i] == 1 and i != vertex)]


def DFS_list(A_list,vertex) :

    visited = [0 for _ in range(len(A_mat))]
    stack = deque()
    visited[vertex] = 1
    stack.append(vertex)

    while stack :
        i = stack[-1]
        flag = True
        for elem in A_list[i] :
            if visited[elem] == 0 :
                visited[elem] = 1
                stack.append(elem)
                flag = False
        if flag :
            stack.pop()
    
    return [i for i in range(len(A_mat)) if (visited[i] == 1 and i != vertex)]
 

if __name__ == "__main__" :
    
    vertex = 4
    A_mat = [[0,1,1,0,0],[1,0,1,0,0],[1,1,0,0,0],[0,0,0,0,1],[0,0,0,1,0]]
    print(DFS_matrix(A_mat,vertex))
    A_list = [[1,2],[0,2],[0,1],[4],[3]]
    print(DFS_list(A_list,vertex))