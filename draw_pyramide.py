def draw_pyramid(n):

    n = n*2
    pyramide = []
    cm = 0
    for i in range(n):

        if i in (0,1,2):
            mid = ['/\\','/__\\','/__:_\\'][i]
        elif i%3 == 0:
            cm+=1
            mid = '/_' + '|__' * cm + '|_\\'
        elif i%3 == 1:
            cm+=1
            mid = '/' + '|__' * cm + '|_\\'
        elif i%3 == 2:
            mid = '/__' + '|__' * cm + '|_\\'

        if i < n//2:
            side = '.' + '´\\' * i
        else:
            side = '\\' + '´\\' * ((n-1) - i)

        if i%2 == 1 and i >= 3:
            side = [i for i in side]
            if i == n//2:
                side[1] = ' '
            elif side[0] == '.':
                side[3] = ' '
        side = ''.join(side)

        layer = side+mid
        layer = ' ' * (int(n*2.5) - (n-i) - len(layer) + 1) + layer + ' ' * (n-i-1)
        pyramide.append(layer)
    return '\n'.join(pyramide)


while 1==1:
    print(draw_pyramid(int(input('  input: '))), '\n')

