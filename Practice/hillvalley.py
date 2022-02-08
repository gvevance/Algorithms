'''
A list of numbers is said to be a hill if it consists of an ascending sequence followed by a descending sequence, 
where each of the sequences is of length at least two. Similarly, a list of numbers is said to be a valley if it 
consists of an descending sequence followed by an ascending sequence. You can assume that consecutive numbers in 
the input sequence are always different from each other.

Write a Python function hillvalley(l) that takes a list l of integers and returns True if it is a hill or a valley, 
and False otherwise. Here are some examples to show how your function should work.

>>> hillvalley([1,2,3,5,4])
True

>>> hillvalley([1,2,3,4,5])
False

>>> hillvalley([5,4,1,2,3])
True

>>> hillvalley([5,4,3,2,1])
False   '''


def hillvalley(l):
  
    crossover = 0
    for i in range(1,len(l)-1):
        if l[i] > l[i-1] and l[i+1] < l[i] :
            crossover += 1
        elif l[i] < l[i-1] and l[i+1] > l[i] :
            crossover += 1
      
    if crossover != 1 :
        return False
    else :
        return True
    