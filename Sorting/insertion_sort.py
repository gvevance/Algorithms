'''
Selection sort is an O(n^2) sorting algorithm. The logic is to go over the array from arr[1] to arr[n-1], 
compare it with the elements to the left, and swap it into the right position (if a swap is needed). At the 
end of the kth iteration, the element arr[k] will be in the right position considering only the elements from 
arr[0...k]. In the worst-case, it takes n(n-1)/2 steps. So O(n^2). '''

def insertion_sort(A,l,r):
    ''' Convention is that array elements are indexed from l to r-1. '''
    
    for i in range(l+1,r):
        j = i
        while A[j] < A[j-1] :
            A[j],A[j-1] = A[j-1],A[j]
            j = j-1
    
    return A

def main():
    try :
        A = list(map(int,input("Enter array (space-separated) : ").split()))
        # Enter array. Split to get individual values. Map each elem to int type.
        # Convert map object to list
    except :
        print("Wrong input entered. Aborting ...")
        exit()

    print(insertion_sort(A,0,len(A)))

if __name__ == "__main__" :
    main()
