def factorial(n):

    # base case should be 0. n=1 is wrong. If testcase contains n=0 => dead.
    if n == 1 :
        return 1

    return n*factorial(n-1)

n = int(input("Enter n : "))
print(factorial(n))