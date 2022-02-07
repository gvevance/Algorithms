''' Worst-case O(nlogn) algorithm even if n is not a power of 2. Drawback is it is not in-place. '''


def merge(L,m,R,n) :
    pass


def merge_sort_rec(A,l,r):
    pass    


def main():
    A = list(map(int,(input("Enter array (space-separated) : ")).split()))
    A_sorted = merge_sort_rec(A,0,len(A))

    print(A_sorted)



if __name__ == "__main__":
    main()