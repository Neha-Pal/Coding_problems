def checkAmstrong(n):
    n_str = str(n)
    n_digit = len(n_str)

    total = 0

    for digit in n_str:
        total += int(digit)**n_digit
    return n == total

n = 123
print(checkAmstrong(n))