#fibonacii
def fibonacii(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacii(n-1) + fibonacii(n-2)
    
n = 4
print(fibonacii(n))