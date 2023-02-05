from math import gcd , lcm , sqrt , floor , ceil
MOD = int(1e9)+7

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
    i = 2
    while i*i<=N:
        if a[i]:
            for j in range(i*i,N+1,i):
                a[j] = 0
        i+=1
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
def factorial(n):
    f = [1 for i in range(n+1)]
    for i in range(1,n+1):
        f[i] = (i*f[i-1])%MOD
    return f

# fastPower
def fast_power(base , pow , MOD , res = 1):
    while pow:
        if pow&1:res = (res*base)%MOD
        base = (base*base)%MOD
        pow//=2
    return res

# instead of dividing by n -> multiplying by mul_inverse(n) 
def mul_inverse(n,mod):
    return fast_power(n,mod-2,mod)

# nCr
def nCr (n,r):
    f = factorial(n)
    return (f[n]*mul_inverse((f[r]*f[n-r])%MOD,MOD))%MOD

# nPr
def nPr (n,r):
    f = factorial(n)
    return (f[n]*mul_inverse(f[n-r],MOD))%MOD

# Build Pascal Triangle
def pascal_triangle(n):
    pascal = [[1]for i in range(n+1)]
    for i in range(1,n+1):
        pascal[i] = [1 for x in range(i+1)]
        for j in range(1,i):
            pascal[i][j] = pascal[i-1][j-1]+pascal[i-1][j]
    return pascal

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

## MOD
# (a+b)%m = ((a%m)+(b%m))%m 
# (a-b)%m = ((a%m)-(b%m)+m)%m 
# (a*b)%m = ((a%m)*(b%m))%m
# (a/b)%m = (a*mulinverse(b))%m


##fast Power
# 2^8  = 256
# 4^4  = 256
# 16^2 = 256
# 256^1 = 256

# ret=1
# 2^10    ret = 1
# 4^5     ret = 4
# 16^2
# 256^1  ret = 4 * 256

# ret=1
# 2^15  ret = 2
# 4^7   ret = 4 * 2 = 8
# 16^3  ret = 16 * 8 = 128
# 256^1 ret = 256 * 128 = 32768



## Fermat little theory: 
# P must be prime number
# (a^p) % p = a  
# (a^p)     = a   (mod p)
# (a^(p-1)) = 1   (mod p)
# (a^(p-2)) = 1/a (mod p)
# mulinv(a,p) = a ^ (p-2)

# ncr(n,r) = n! / (r! * (n-r)!)
# ncr(n,r) = n! * mulinv( (r! * (n-r)!))
# npr(n,r) = n! / (n-r)!
# npr(n,r) = n! * mulinv( (n-r)!)
# ncr(n,i) = ncr(n, n-i)
# ncr(n,0) + ncr(n,1) + ncr(n,2) + ....... + ncr(n,n) = 2^n
# npr(n,r) = ncr(n,r) * r! 