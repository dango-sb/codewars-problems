from math import factorial


def var(expr):
    for i in range(1, len(expr)):  # define a
        if expr[i] in '+-' and i != 1:
            j = i
            break
    a = expr[1:j]
    if '-' in a:
        a = (-1, a[1:-1], a[-1])
    else:
        a = (1, a[0:-1], a[-1])
    if a[1] == '':
        a = (a[0], 1, a[2])
    else:
        a = (a[0], int(a[1]), a[2])

    for i in range(j, len(expr)):  # define b
        if expr[i] == ')':
            k = i
            break
    b = expr[j:k]
    if '-' in b:
        b = (-1, int(b[1:]))
    else:
        b = (1, int(b[1:]))

    for i in range(k, len(expr)):   # define n
        if expr[i] == '^':
            m = i
            break
    n = int(expr[m+1:])

    return a, b, n


def cmb(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def expand(expr):
    a, b, n = var(expr)
    res = []
    for k in range(0, n + 1):
        if n-k != 0:
            if n-k == 1:
                v = a[2]
            else:
                v = a[2] + '^' + str(n-k)
        else:
            v = ''

        num = str(cmb(n, k) * (a[1] ** (n-k)) * (b[1] ** k))
        if num == '1' and v != '':
            num = ''
        s = ['-' if (a[0] ** (n-k)) * (b[0] ** k) == -1 else '+'][0]
        if s[0] == '+' and k == 0:
            s = ''
        res.append(s+num+v)

    return ''.join(res)

while True:
    print(expand(input("   :")))

