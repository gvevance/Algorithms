'''
Depth first search. 2 variants - Adjacency matrix and list to represent graph. O(n^2) in n vertices for Adj matrix ; 
O(m+n) for Adj list when m = number of edges in the graph, n = number of nodes (assuming m << n^2). DFS is inherently 
recursive in nature. '''

from collections import deque


def DFS_list(A,vertex,visited) :
    
    visited[vertex] = 1
    for elem in [i for i in A[vertex] if visited[i] == 0] :
        DFS_list(A,elem,visited)


def DFS_matrix(A,vertex,visited) :

    visited[vertex] = 1
    for j in range(len(A)) :
        if A[vertex][j] == 1 and visited[j] == 0 :
            DFS_matrix(A,j,visited)


def DFS(A,vertex,list) :

    visited = [0 for _ in range(len(A))]        # doesn't matter if A is a matrix or list

    if list == True :
        DFS_list(A,vertex,visited)

    else :
        DFS_matrix(A,vertex,visited)
    
    return [i for i in range(len(A)) if (visited[i] == 1 and i != vertex)]


if __name__ == "__main__" :
    
    vertex = 2
    A_mat = [[0,1,0],[1,0,0],[0,0,0]]
    print(DFS(A_mat,vertex,list=False))
    A_list = [[1],[0],[]]
    print(DFS(A_list,vertex,list=True))
    # print(DFS_list_pre_post(A_list,vertex))
