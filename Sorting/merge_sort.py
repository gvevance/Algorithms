''' Worst-case O(nlogn) algorithm even if n is not a power of 2. Drawback is it does not sort in-place. '''


def merge(L,m,R,n) :
    
    i = j = k = 0
    merged=[]

    while(k < m+n):                     # merged array is completely filled

        if (j == n) :                   # Note : we must check these conditions first
            merged.append(L[i])
            i,k = i+1,k+1
        
        elif (i == m)  :                # Note : we must check these conditions first
            merged.append(R[j])
            j,k = j+1,k+1

        elif L[i] <= R[j] :
            merged.append(L[i])
            i,k = i+1,k+1

        elif L[i] > R[j] :
            merged.append(R[j])
            j,k = j+1,k+1

    return merged


def merge_sort_rec(A,l,r):
    
    if l == r-1 :
        return [A[l]]                   # must return it as an array and not the number

    mid = (l+r)//2                      # integer division
    L = merge_sort_rec(A,l,mid)         # not chopping into pieces but the indices at the virtual chops are sent
    R = merge_sort_rec(A,mid,r)

    return merge(L,mid-l,R,r-mid)       # mid-l and r-mid are the sizes of L and R pieces    


def main():
    A = list(map(int,(input("Enter array (space-separated) : ")).split()))
    A_sorted = merge_sort_rec(A,0,len(A))

    print(A_sorted)

    if sorted(A) == A_sorted :
        print("\nSort algorithm successful.\n")
    else :
        print("\nSort algorithm unsuccessful.\n")



if __name__ == "__main__":
    main()