'''Moving Intervals

Zonal Computing Olympiad 2018

There are C cakes in a row, numbered from 1 to C. There are N children, each of whom have selected a consecutive set 
of cakes to eat. That is, Child i has decided to eat all the cakes from Si to Ei, end points inclusive. If there is a 
cake which appears in some two childrens' set, then they will fight because both of them want to eat that cake, and 
you don't want that to happen. You will be given an integer K which will be either 0 or 1. If K is 0, then you should 
find out if some two children will fight. Print "Good" if no one fights, and "Bad" if someone fights.

If K is 1, then you can persuade at most one child to change his decision to some other set of cakes. But the number 
of cakes that he eats must be the same. That is, if Child i had initially decided that he wants to eat the cakes from 
Si to Ei, then you could persuade the child to instead eat the cakes from X to Y instead, for any valid X and Y 
(ie. 1 ≤ X ≤ Y ≤ C), provided that the number of cakes is the same (ie. Ei - Si + 1 = Y - X + 1). If after persuading 
at most 1 Child to change his decision, no fights happen, then print "Good". But if no matter what you do, someone 
will fight, then print "Bad".

Solution hint
Sort the intervals and check for overlaps.

Input format
The first line of each test case contains three integers C, N and K denoting the number of cakes, number of children and K, respectively.

The i-th of the next N lines contains two space separated integers Si and Ei which denotes the initial decision of Child i. That is, Child i wants to eat from cake Si to cake Ei.

Output format
For each test case, output a single line containing "Good" or "Bad".

Constraints
1 ≤ T ≤ 10
1 ≤ C ≤ 10^9
1 ≤ N ≤ 10^5
0 ≤ K ≤ 1
1 ≤ Si, Ei ≤ C

Sample input 1

5 2 0
2 2
3 5

Sample output 1
Good

Sample input 2
5 2 1
2 2
2 5

Sample output 2
Good

Sample input 3
5 2 1
2 3
2 5

Sample output 3
Bad

'''

# steps :
# 1. arrange in sorted order 
# 2. examne to see overlaps
# 3. k=1 then check if overlap can be avoided

def merge(L,m,R,n):

    i,j,k = 0,0,0
    C = []

    while (k < m+n):
        if i==m :
            C.append(R[j])
            j,k = j+1,k+1
        
        elif j==n :
            C.append(L[i])
            i,k = i+1,k+1

        elif L[i][0] <= R[j][0] :
            C.append(L[i])
            i,k = i+1,k+1

        elif L[i][0] > R[j][0] :
            C.append(R[j])
            j,k = j+1,k+1

    return C


def merge_sort(A,l,r):

    if l >= r-1 :
        return [A[l]]

    mid = (l+r)//2 
    L = merge_sort(A,l,mid)
    R = merge_sort(A,mid,r)

    return merge(L,mid-l,R,r-mid)


C,N,K = list(map(int,input().split()))

cake_list = []
for i in range(N):
    cakes = list(map(int,input().split()))
    cake_list.append(cakes)
# print(cake_list)

# sort based on first values of elemenets of list
cake_list_s = merge_sort(cake_list,0,N)
print(cake_list_s)

if K == 0 :     # just check if there is no overlap
    for idx in range(N-1):
        if cake_list_s[idx+1][1] > cake_list_s[idx][1] :
            continue
        else :
            print("Bad")
            exit()
    print("Good")
    exit()

elif K == 1 :
    
    # case 1 - if some chunk has overlap on both sides, it has to be moved to some other vacant spot
    # case 2 - if overlap is only on one side
    
    count = 0
    gaps_list = []      # size will be N+1

    gaps_list.append([cake_list_s[0][1] - 1])       # store left-most gap

    for idx in range(1,N-1):
        pass
            

         


