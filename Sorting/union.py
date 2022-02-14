'''
Set union between 2 sets. Variation of the merge function from mergesort. '''

def set_union(A,B) :
    ''' returns set union A U B '''

    A_s = list(set(A))
    B_s = list(set(B))
    A_s.sort()
    B_s.sort()
    C = []

    m,n = len(A_s),len(B_s)
    i,j = 0,0

    while ( i+j < m+n ) :

        if i == m :
            C.append(B_s[j])
            j += 1
        
        elif j == n :
            C.append(A_s[i])
            i += 1

        elif A_s[i] < B_s[j] :
            C.append(A_s[i])
            i += 1

        elif A_s[i] > B_s[j] :
            C.append(B_s[j])
            j += 1

        elif A_s[i] == B_s[j] :
            C.append(A_s[i])
            i,j = i+1,j+1
    
    return C

if __name__ == "__main__" :

    A = list(map(int,(input("Enter array A (space-separated) : ")).split()))
    B = list(map(int,(input("Enter array B (space-separated) : ")).split()))

    print(set_union(A,B))