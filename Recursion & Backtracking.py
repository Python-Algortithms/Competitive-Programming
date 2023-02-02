import sys
sys.stdin = open("D:\Kaldesh\input.txt",'r')
sys.stdout = open("D:\Kaldesh\output.txt",'w')

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

# Generate all combinations choose m elements from n
cnt = 0
def combinations(a,n,m,idx=0,path = []):
    if idx == n:
        global cnt
        if cnt == m:
            print(path)
        return

    cnt +=1
    path.append(a[idx])
    combinations(a,n,m,idx+1)
    path.pop()
    cnt-=1
    combinations(a,n,m,idx+1)

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

# Generate all subsequences
def subset(a,n,idx = 0):
    if idx == n:
        return

    a.append(idx) # DO
    subset(idx+1) # call
    a.pop() #UNDO
    subset(idx+1) # call 

