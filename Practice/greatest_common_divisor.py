'''

Programming and DSA using Python NPTEL

Naive algo is straight-forward. But with some ideas to optimise for time taken.
Euclid's algorithm is a much more efficient recursive (or iterative) algorithm. '''


def gcd_naive(m,n):
    
    # 1 is a common factor at the very least
    for i in range(min(m,n),0,-1):
        if (m%i) == 0 and (n%i) == 0 :
            break
    
    return i


def gcd_euclid_rec(m,n):
    ''' Recursive formulation'''

    # algo needs m>=n so enforce it in the first step
    if m < n :
        m,n = n,m

    if m%n == 0 :
        return n

    else :
        return (gcd_euclid_rec(n,m%n))
    

def gcd_euclid_iter(m,n):
    ''' Iterative formulation '''

    # algo needs m>=n so enforce it in the first step
    if m < n :
        m,n = n,m

    while (True):   # no need of condition - at n=1 it will break if it didn't already
        if m%n == 0:
            break
        else :
            m,n = n,m%n
    
    return n


def main():
    m = int(input("Enter first number : "))
    n = int(input("Enter second number : "))

    print(gcd_naive(m,n))
    print(gcd_euclid_rec(m,n))
    print(gcd_euclid_iter(m,n))


if __name__ == "__main__" :
    main()    
