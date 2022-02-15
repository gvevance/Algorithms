'''
Breadth first search. 2 variants - Adjacency matrix and list to represent graph. O(n^2) in n vertices for Adj matrix ; 
O(m+n) for Adj list when m = number of edges in the graph, n = number of nodes (m << n^2). '''

from collections import deque

def BFS_matrix(A,vertex):
    ''' A = adjacency matrix
        vertex = vertex to search path to '''

    Q = deque()
    visited = []
    for _ in range(len(A)) :
        visited.append(0)

    Q.append(vertex)
    visited[vertex] = 1

    while Q :
        i = Q.popleft()
        for j in range(len(A)) :
            if A[i][j] == 1 and visited[j] == 0 :
                visited[j] = 1
                Q.append(j)
    
    return [i for i in range(len(A)) if ( visited[i] and i != vertex ) ]

if __name__ == "__main__" :
    
    A = [[0,1,1,0,1],[1,0,1,0,0],[1,1,0,1,0],[0,0,1,0,1],[1,0,0,1,0]]
    print(BFS_matrix(A,0))
    