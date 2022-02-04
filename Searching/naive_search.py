'''
This is the naive search algorithm where you go through all elements in an array or list.
It does not matter which data structure the elements are stored in, if the elements are 
not sorted. You have to access each of the n elements in the worst case. The complexity 
is thus O(n) for an n-element list or array.'''


def naive_search(k,A,l,r):
    ''' k is the element to search for. A is the array. l and r are the left and right 
    endpoints of the array with the convention that we want to search within indices 
    l and r-1 , both included. This function returns a boolean and an integer. The boolean 
    corresponding to whether k was found in A. The integer being the index in A that k 
    was found in. -1 is sent if k was not found.'''

    for index in range(l,r):
        if A[index] == k :
            return True , index

    return False , -1


def main():

    try :
        A = list(map(int,input("Enter array (space-separated) : ").split()))
        # Enter array. Split to get individual values. Map each elem to int type.
        # Convert map object to list
        k = int(input("Enter element to search for : "))
    except :
        print("Wrong input entered. Aborting ...")
        exit()

    found , index = naive_search(k,A,0,len(A))

    if found :
        print(f"{k} found at index {index}.")
    else :
        print(f"{k} not found in the array.") 


if __name__ == "__main__" :
    main()