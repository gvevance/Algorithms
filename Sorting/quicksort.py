''' Worst-case O)n^2) but O(nlogn) on average-case. Sorts in place but is not stable (swaps involved).
    Recursive as well as iterative versions possible. '''


def partition(A,l,r) :
    ''' Convention is : A[l:lptr] is lower, A[lptr+1:r] is upper, pivot at A[lptr] '''

    lptr = uptr = l+1
    
    # partitioning into lower and upper
    while(uptr < r):
    
        if A[uptr] <= A[l] :                    # pivot chosen at index l
            A[uptr],A[lptr] = A[lptr],A[uptr]
            lptr , uptr =  lptr+1 , uptr + 1
        
        else :
            uptr += 1
        
    # move pivot to the right position
    lptr = lptr - 1
    A[l] , A[lptr] = A[lptr] , A[l]
    
    return lptr


def quicksort_rec(A,l,r):

    if l >= r-1 :       # l = r when the pivot happens to be an extreme value
        return A

    lptr = partition(A,l,r)
    A = quicksort_rec(A,l,lptr)
    A = quicksort_rec(A,lptr+1,r)
    
    return A


def main():
    A = list(map(int,(input("Enter array (space-separated) : ")).split()))
    A_sorted = quicksort_rec(A,0,len(A))

    print(A_sorted)

    if sorted(A) == A_sorted :
        print("\nSort algorithm successful.\n")
    else :
        print("\nSort algorithm unsuccessful.\n")
    


if __name__ == "__main__":
    main()