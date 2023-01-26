import sys
sys.stdin = open("D:\Kaldesh\input.txt",'r')
sys.stdout = open("D:\Kaldesh\output.txt",'w')

# Backtracking

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

a = [0 for i in range(5)]
n = len(a)
v = [0 for i in range(n+1)]

all_permutations(0 , a , v , n)
all_possible_solution(0 , a , n)