from math import gcd , lcm , sqrt , floor , ceil

# find last digit from -> (n^m)
def last_digit(n,m) -> int: # O(1)
    if m%4==1:
        print(n%10)
    elif m%4==2:
        print(n**2%10)
    elif m%4==3:
        print(n**3%10)
    else:
        print(n**4%10)

# find divisors of a number
def divisors(n) -> list:
    d = []
    i = 1
    while i*i<=n: #O(sqrt(n))
        if n%i==0:
            d.append(i)
            if i*i != n: # for a square num
                d.append(n//i)
        i+=1
    return d

# check if prime
def prime(n) -> bool:
    if n < 2:
        return False
    i = 2
    while i*i<=n: #O(sqrt(n))
        if n%i == 0:
            return False
        i+=1
    return True

# Sieve
def sieve(N) -> list:
    #O(sqrt(N)*log(log(n))) ~= O(N)
    a , p = [1 for i in range(N+1)] , []
    a[0] = a[1] = 0 
    for i in range(2,int(N**(1/2))+1): 
        if a[i]:
            for j in range(i*i,N+1,i):
                a[j] = 0
    for i in range(2,len(a)):
        if a[i]:p.append(i)
    return p

# Any Even number > 2 can be expressed as a sum of 2 prime numbers
def Goldbach(n) -> None:
    p = sieve(n)
    for i in range(2,len(p)):
        if p[i] and p[n-i]:
            print(i,n-i);return

# Express any number as a multiplication of prime numbers
def factorization(n) -> list:
    factors = []
    N = int(1e6)
    p = sieve(N)
    for i in p: # O(sqrt(N))
        if n == 1 or i*i > n:break
        while n%i==0:
            factors.append(i)
            n//=i
    if n>1:factors.append(n)
    return factors

# Co-Primes GCD (x,y) = 1
def co_primes(x,y) -> bool:
    return gcd(x,y) == 1

# factorial
def factorial(n , mod):
    f = [1 for i in range(n+1)]
    for i in range(1,n+1):
        f[i] = ((i%mod)*(f[i-1]%mod))%mod
    return f


# find last digit from (n^m)
# you notice that the this problem can be solved using remainder
# the last digit is repeated every four time 

# base(2)       base(3)
# 1 = 2         1 = 3
# 2 = 4         2 = 9
# 3 = 8         3 = 27
# 4 = 16        4 = 81
# 5 = 32        5 = 243
# 6 = 64        6 = 729
# 7 = 128       7 = 2187
# 8 = 256       8 = 6561


# To Know number of divisors using factorization
# num : 60
# 2 * 2 * 3 * 5   = {2:2 , 3:1 , 5:1}
# no. of divisors = (2+1)*(1+1)*(1+1) = 12



# To Know GCD from fatorization
# 60 : 2^2 * 3^1 * 5^1
# 36 : 2^2 * 3^2 * 5^0
# GCD = min(2^2,2^2)*min(3^1,3^2)*min(5^1,3^0) = 12

# To Know LCM from fatorization
# 60 : 2^2 * 3^1 * 5^1
# 36 : 2^2 * 3^2 * 5^0
# GCD = max(2^2,2^2)*max(3^1,3^2)*max(5^1,3^0) = 180

# LCM (x,y) = (x*y) / GCD(x,y)
# Fact:LCM of co-primes(x,y) = x*y


