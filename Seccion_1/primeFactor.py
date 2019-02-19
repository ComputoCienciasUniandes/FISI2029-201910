def primeFactors_CORTA(n):
    ret = ''
    for i in range(2, n + 1):
        num = 0
        while(n % i == 0):
            num += 1
            n /= i
        if num > 0:
            ret += '({}{})'.format(i, '**%d' % num if num > 1 else '')
        if n == 1:
            return ret
       
import numpy as np

def new_is_prime(n):
    result=True
    for i in range(2,int(np.sqrt(n)+1)):
        if n%i==0:
            result = False
    return result

def get_prime_Factors(n):
    if type(n) is not int or n < 1:
        # Not an integer, negative or 0
        return []
    elif(n<3):
        return [n]
    factors=[]
    if new_is_prime(n):
        return [n]
    while(n>1):
        for i in range(2,n+1):
            if new_is_prime(i) and not n % i:
                n=int(n/i)
                factors.append(i)
                break
    return factors

def primeFactors_larga(n):
    f= get_prime_Factors(n)
    factors = sorted(list(set(f)))
    powers = [f.count(factor) for factor in factors]
    result=""
    for i in range(len(factors)):
        result+="({}{})".format(factors[i],"**%d" % powers[i] if powers[i]>1 else "" )
    return result