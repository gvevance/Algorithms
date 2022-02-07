import time

dic = { 1:1 ,
        2:1 }   # base cases

def fibonacci(n,smart=False) :
    ''' this is a really really bad recursive algorithm - O(2^n)'''

    if smart :
        if n not in dic :
            ans = fibonacci(n-1,smart) + fibonacci(n-2,smart)
            dic[n] = ans
        else :
            ans = dic[n]
    
    else :

        if n == 1 or n == 2 :       # base cases
            return 1
        else :
            ans = fibonacci(n-1,smart) + fibonacci(n-2,smart)

    return ans

n = int(input("Enter n : "))
start1 = time.time()
print(fibonacci(n))
end1 = time.time()
print(f"Time for bad algo = {end1-start1}")

start1 = time.time()
print(fibonacci(n,smart=True))
end1 = time.time()
print(f"Time for good algo = {end1-start1}")