'''
This is the binary search algorithm where only have to go through log2(n) elements in a sorted 
array to ascertain if an element exists in the array or not. The data structure the elements 
are stored in must be array so that each element can be accessed in O(1) time. You have to 
access log2(n) elements, each in O(1) time, in the worst-case. The complexity is thus O(log2(n)) 
for an n-element list or array.'''


def binary_search(k,A,l,r):
    ''' k is the element to search for. A is the array. l and r are the left and right 
    endpoints of the array with the convention that we want to search within indices 
    l and r-1 , both included. This function returns a boolean and an integer. The boolean 
    corresponding to whether k was found in A. The integer being the index in A that k 
    was found in. -1 is sent if k was not found.'''

    if l == r :
        return False , -1

    start , end = l,r-1

    while (start <= end):           
    # when start=end, mid=start=end. if k isn't found still, either start will be updated 
    # to a value equivalent to end+1 or end will get updated to start-1. Both cases end up 
    # in control exiting from the while loop and False is returned.  

        mid = (start + end)//2      # integer division

        if A[mid] == k :
            return True , mid
        elif A[mid] > k :
            end = mid - 1       # mid is excluded
        else :
            start = mid + 1     # mid is excluded

    return False , -1


def main():
    try :
        A = list(map(int,input("Enter array (space-separated, NEED NOT BE SORTED) : ").split()))
        # Enter array. Split to get individual values. Map each elem to int type.
        # Convert map object to list
        k = int(input("Enter element to search for : "))
    except :
        print("Wrong input entered. Aborting ...")
        exit()

    A.sort()    # sort the array in place if it is not entered sorted
    found , index = binary_search(k,A,0,len(A))

    if found :
        print(f"{k} found at index {index}.")
    else :
        print(f"{k} not found in the array.") 


if __name__ == "__main__" :
    main()