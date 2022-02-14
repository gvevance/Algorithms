''' Worst-case O)n^2) but O(nlogn) on average-case. Sorts in place but is not stable (swaps involved).
    Recursive as well as iterative versions possible. '''

import random

def partition(A,l,r,random_pivot) :
    ''' Convention is : A[l:lptr] is lower, A[lptr+1:r] is upper, pivot at A[lptr] unless randomised. '''

    if random_pivot :
        # random pivot each time
        piv = random.randint(l,r-1)
        A[piv],A[l] = A[l],A[piv]

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


def quicksort_rec(A,l,r,random_pivot = False):

    if l >= r-1 :       # l = r when the pivot happens to be an extreme value
        return

    lptr = partition(A,l,r,random_pivot)
    quicksort_rec(A,l,lptr)
    quicksort_rec(A,lptr+1,r)


def main():
    A = list(map(int,(input("Enter array (space-separated) : ")).split()))
    quicksort_rec(A,0,len(A),True)

    print(A)

    if sorted(A) != A :
        print("\Wrong output.\n")


if __name__ == "__main__":
    main()