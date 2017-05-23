import sys
sys.setrecursionlimit(1000000000)
print("Fibonacci-Recursivo")

def fibR(n):
  if n==1 or n==2:
    return 1
  return fibR(n-1)+fibR(n-2)

fibR(0)
