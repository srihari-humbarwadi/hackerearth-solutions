from math import sqrt

def isprime(x):
    for i in range(2, int(sqrt(x))+1):
        if x%i == 0:
            return False
    return True

x = int(input())
for X in range(2,x+1):
    if isprime(X):
        print(X, end=' ')