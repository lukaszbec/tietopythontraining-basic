def power(a, n):
    if n == 0:
        return 1
    if n > 1:
        n = n - 1
        a = a * power(a, n)
        return a
    else:
        return a


aa = float(input())
nn = int(input())

print(power(aa, nn))
