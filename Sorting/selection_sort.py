''' 
Selection sort is an O(n^2) sorting algorithm. The logic is to find the smallest element in 
the unsorted portion of the array and swapping it in the right position. In the worst-case 
it takes n(n+1)/2 accesses. '''

def selsort(A,l,r):
    ''' Convention is that array elements are indexed from l to r-1.'''

    for i in range(l,r-1):
        next_smallest_idx = i
        for j in range(i+1,r):
            if A[j] < A[next_smallest_idx] :
                next_smallest_idx = j
        A[i],A[next_smallest_idx] = A[next_smallest_idx],A[i]
    
    return A

def main():
    try :
        A = list(map(int,input("Enter array (space-separated) : ").split()))
        # Enter array. Split to get individual values. Map each elem to int type.
        # Convert map object to list
    except :
        print("Wrong input entered. Aborting ...")
        exit()

    A_sorted = selsort(A,0,len(A))
    print(A_sorted)
    
    if sorted(A) != A_sorted :
        print("\Wrong output.\n")

if __name__ == "__main__" :
    main()
            

