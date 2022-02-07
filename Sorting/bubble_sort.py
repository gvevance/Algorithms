'''
Bubble sort is not a something we would normally do intuitively. Start from arr[0] to the right. When the cursor 
is at i, compare A[i] and A[i+1] and swap them if needed. At the end of the kth iteration, the largest k elements 
will all be in their right positions and we do not need to compare with them. Worst case - (n)(n-1)/2 compare + 
swaps. So O(n^2).  
'''

def bubble_sort(A,l,r) :
    ''' Convention is that array elements are indexed from l to r-1. '''

    for i in range(1,l+r+1) :

        # Last i-1 elements are already in place
        for j in range(l,r-i) :
            if A[j] > A[j+1] :
                A[j],A[j+1] = A[j+1],A[j]

    return A

def bubble_sort_optimised(A,l,r) :
    ''' Convention is that array elements are indexed from l to r-1. GeeksForGeeks. It can be optimized by 
    stopping the algorithm if inner loop didn’t cause any swap at any iteration of i. '''

    for i in range(1,l+r+1) :
        swapped = False

        # Last i-1 elements are already in place
        for j in range(l,r-i) :
            if A[j] > A[j+1] :
                A[j],A[j+1] = A[j+1],A[j]
                swapped = True

        ''' IF no two elements were swapped by the inner loop in any iteration of i, then break. This indicates 
        sorting is complete and we don't need to keep comparing elements. '''
        if swapped == False:
            break

    return A

def main():
    try :
        A = list(map(int,input("Enter array (space-separated) : ").split()))
        # Enter array. Split to get individual values. Map each elem to int type.
        # Convert map object to list
    except :
        print("Wrong input entered. Aborting ...")
        exit()

    A_sorted = bubble_sort(A,0,len(A))
    print(A_sorted)
    
    if sorted(A) == A_sorted :
        print("\nSort algorithm successful.")
    else :
        print("\nSort algorithm unsuccessful.")

    A_sorted = bubble_sort_optimised(A,0,len(A))
    print(A_sorted)
    
    if sorted(A) == A_sorted :
        print("\nSort algorithm successful.")
    else :
        print("\nSort algorithm unsuccessful.")

if __name__ == "__main__" :
    main()
