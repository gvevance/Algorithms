''' Worst-case O)n^2) but O(nlogn) on average-case. Sorts in place but is not stable (swaps involved).
    Recursive as well as iterative versions possible. '''


def partition(L,m,R,n) :
    pass


def quicksort_rec(A,l,r):
    pass    


def main():
    A = list(map(int,(input("Enter array (space-separated) : ")).split()))
    A_sorted = quicksort_rec(A,0,len(A))

    print(A_sorted)



if __name__ == "__main__":
    main()