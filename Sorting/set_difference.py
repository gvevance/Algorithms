'''
Set difference between 2 sets. Variation of the merge function from mergesort. '''

def set_diff(A,B) :
    ''' returns set difference A-B '''

    A_s = list(set(A))
    B_s = list(set(B))
    A_s.sort()
    B_s.sort()
    C = []

    m,n = len(A_s),len(B_s)
    i,j = 0,0

    while(i+j < m+n) :

        if i == m :
            break
        
        elif j == n :
            C.append(A[i])
            i += 1

        elif A[i] < B[j] :
            C.append(A[i])
            i += 1

        elif A[i] > B[j] :
            j += 1

        elif A[i] == B[j] :
            i,j = i+1,j+1
    
    return C

if __name__ == "__main__" :

    A = list(map(int,(input("Enter array A (space-separated) : ")).split()))
    B = list(map(int,(input("Enter array B (space-separated) : ")).split()))

    print(set_diff(A,B))