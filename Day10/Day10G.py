import sys
sys.setrecursionlimit(5000)

n = int(input('Enter limit:'))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print('The factorial of',n , 'is',factorial(n))
