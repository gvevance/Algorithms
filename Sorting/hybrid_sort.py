''' Mix and match algorithms. O(nlogn) algo when size is large. O(n^2) algo when the size becomes < 16 or so.'''


def hybrid_sort_rec(A,l,r):
    pass    


def main():
    A = list(map(int,(input("Enter array (space-separated) : ")).split()))
    A_sorted = hybrid_sort_rec(A,0,len(A))

    print(A_sorted)



if __name__ == "__main__":
    main()