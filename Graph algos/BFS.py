'''
Breadth first search. 2 variants - Adjacency matrix and list to represent graph. O(n^2) in n vertices for Adj matrix ; 
O(m+n) for Adj list when m = number of edges in the graph, n = number of nodes (m << n^2). '''

from collections import deque

def BFS_matrix(A_mat,vertex):
    ''' A_mat = adjacency matrix
        vertex = vertex to search path to '''

    Q = deque()
    visited = [0 for _ in range(len(A_mat))]

    Q.append(vertex)
    visited[vertex] = 1

    while Q :
        i = Q.popleft()
        for j in range(len(A_mat)) :
            if A_mat[i][j] == 1 and visited[j] == 0 :
                visited[j] = 1
                Q.append(j)
    
    return [i for i in range(len(A_mat)) if ( visited[i] and i != vertex ) ]


def BFS_list(A_list,vertex) :
    ''' A_list = adjacency list
        vertex = vertex to search path to '''

    visited = [0 for _ in range(len(A_list))]
    Q = deque()
    Q.append(vertex)

    while Q :
        i = Q.popleft()
        for j in A_list[i] :
            if visited[j] == 0 :
                visited[j] = 1
                Q.append(j)
    
    return [i for i in range(len(A_list)) if (visited[i] == 1 and i != vertex)]


if __name__ == "__main__" :
    
    vertex = 3
    A_mat = [[0,1,1,0,0],[1,0,1,0,0],[1,1,0,0,0],[0,0,0,0,1],[0,0,0,1,0]]
    print(BFS_matrix(A_mat,vertex))
    A_list = [[1,2],[0,2],[0,1],[4],[3]]
    print(BFS_list(A_list,vertex))