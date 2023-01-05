import math
import time
from functools import lru_cache


def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f += 6
    return True


def primes(a, b):
    """Returns prime numbers between two integers"""
    if a > b:
        return primes(b, a)
    c = []
    if a>1000000000 or b>1000000000:
      return c
    for n in range(a, b+1):
        if is_prime(n):
            c.append(n)
    return c


def prime_factors(n):
    import math
    p = [
        {"f": 1, "s": 1},
    ]
    if n>1000_000_000_000_000:
        return p
    while n % 2 == 0:
        if p[-1]['f']!=2:
            p.append({"f": 2, "s": 1})
        else:
            p[-1]['s']+=1 
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while (n % i == 0):
            if p[-1]['f']!=i:
                p.append({"f": int(i), "s": 1})
            else:
                p[-1]['s']+=1 
            n = n / i
    if n > 2:
        if p[-1]['f']!=n:
            p.append({"f": int(n), "s": 1})
        else:
            p[-1]['s']+=1
    if len(p)>1:
        p=p[1:]
    return p


@lru_cache()
def factoriel(nb):
    if nb>1000:
        return "Huge Number !"
    if nb == 0 or nb == 1:
        return 1
    return nb*factoriel(nb-1)


def pgcd(a, b):
    if a < b:
        return pgcd(b, a)
    if b == 0:
        return a
    return pgcd(b, a % b)

def ppmc(a, b):
    return a*b/pgcd(b, a)

def etendu(a, b):
    x, y, xx, yy = 1, 0, 0, 1
    while b > 0:
        q = a//b
        a, b = b, a % b
        xx, x = x-q*xx, xx
        yy, y = y-q*yy, yy
    y = -y
    return a, x, y


@lru_cache()
def fibbonacci(n):
    if n>1000:
        return "Huge Number"
    if n <= 0:
        return 0
    if n < 3:
        return 1
    return fibbonacci(n-1)+fibbonacci(n-2)