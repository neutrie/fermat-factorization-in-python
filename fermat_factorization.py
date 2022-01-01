import math

def fermat_factorization(NUM):
    print('x\tx\u00b2\t\tx\u00b2-n\ty=sqrt(x\u00b2-n)')
    x = math.ceil( math.sqrt(NUM) )
    if NUM == x**2:
        print(f'{NUM} = {x} * {x}')
        return
    else:
        x += 1

    while (x != (NUM+1)/2):
        y = math.sqrt(x**2-NUM)
        print(f'{x}\t{x**2}\t{x**2 - NUM}\t{y}')
        if y == int(y):
            y = int(y)
            print(f'{NUM} = {x}\u00b2 - {y}\u00b2')
            print(f'({x}-{y}) * ({x}+{y}) = {x-y}*{x+y} = {(x-y)*(x+y)}')
            break
        else:
            x += 1

num = int(input('NUM: '))
fermat_factorization(num)
