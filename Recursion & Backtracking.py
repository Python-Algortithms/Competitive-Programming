import sys
sys.stdin = open("D:\Kaldesh\input.txt",'r')
sys.stdout = open("D:\Kaldesh\output.txt",'w')

##### Some Algorithms Implemented using Recursion ######

# Binary Search
def BS (a , l , r , tg):
    if l >= r:return 0
    m = (l+r)//2
    if a[m] < tg:
        l = m+1
    elif a[m] > tg:
        r = m-1
    else:
        return 1

    return BS (a , l , r , tg)

######## Backtracking #######

# def func_name (para = initial):
#    if (stop condition):
#         Action
#         Return 
#     
#     from i to j:
#      DO
#      func_name(para+1)
#      UNDO   
#

# Generate all permutations from 1 -> n
def all_permutations(idx , a ,v, n):
    if idx == n:
        for i in range(n):
            print(a[i],end=" ")
        print()
        return

    for i in range(n):
        if not v[i]:
            a[idx] = i+1
            v[i] = 1
            all_permutations(idx+1 , a ,v, n)
            v[i] = 0

# Generate all Possible Solutions
def all_possible_solution(idx , a , n):
    if idx == n:
        for i in range(n):
            print(a[i],end=" ")
        print()
        return

    for i in range(n):
        a[idx] = i
        all_possible_solution(idx+1 , a , n)

def subset(a,n,idx = 0):
    if idx == n:
        return

    a.append(idx)
    subset(idx+1)
    a.pop()
    subset(idx+1) 

