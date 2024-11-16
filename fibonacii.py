def fibonacii(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacii(n-1) + fibonacii(n-2)
    
n = 4
print(fibonacii(n))