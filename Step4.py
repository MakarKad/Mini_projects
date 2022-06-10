def truex(a):
    return a == 'x'


def trueo(a):
    return a == '0'


fgx = ''
fgo = ''
m = [['p', 'p', 'p'], ['p', 'p', 'p'], ['p', 'p', 'p']]
h = False
a = ''
while not fgx and not fgo:
    c = -1
    if a:
        a = (["A", "B", "C"].index(a[0]), int(a[1]) - 1)
        if m[a[0]][a[1]] == 'p':
            m[a[0]][a[1]] = 'x' if h else '0'
    h = not h
    for i in range(1, 4):
        print(f'       {i}       ', end='' if i != 3 else '\n')
    for i in range(0, 9):
        if i % 3 == 0:
            print('-', end='')
            for j in range(3):
                print('---------------', end=('' if j != 2 else '\n'))
            c += 1
        print('|',
              end=f'       {m[c][0]}      ' if m[c][0] != 'p' and (i == 1 or i == 4 or i == 7) else '              ')
        print('|',
              end=f'       {m[c][1]}      ' if m[c][1] != 'p' and (i == 1 or i == 4 or i == 7) else '              ')
        print('|',
              end=f'       {m[c][2]}      ' if m[c][2] != 'p' and (i == 1 or i == 4 or i == 7) else '              ')
        print('|', end='\n' if i != 1 and i != 4 and i != 7 else '  ')
        if i == 1:
            print('A')
        if i == 4:
            print('B')
        if i == 7:
            print('C')
        if i == 8:
            print('-', end='')
            for j in range(3):
                print('---------------', end=('' if j != 2 else '\n'))
    r = ()
    for i in m:
        r += (*i,)
    rwx1 = all(map(truex, r[:3]))
    rwx2 = all(map(truex, r[3:6]))
    rwx3 = all(map(truex, r[6:]))
    clx1 = all(map(truex, r[::3]))
    clx2 = all(map(truex, r[1::3]))
    clx3 = all(map(truex, r[2::3]))
    dix1 = all(map(truex, r[::4]))
    dix2 = all(map(truex, r[2::2][:-1]))
    if any([rwx1, rwx2, rwx3, clx1, clx2, clx3, dix1, dix2]):
        fgx = 'Player x'
    rwo1 = all(map(trueo, r[:3]))
    rwo2 = all(map(trueo, r[3:6]))
    rwo3 = all(map(trueo, r[6:]))
    clo1 = all(map(trueo, r[::3]))
    clo2 = all(map(trueo, r[1::3]))
    clo3 = all(map(trueo, r[2::3]))
    dio1 = all(map(trueo, r[::4]))
    dio2 = all(map(trueo, r[2::2][:-1]))
    if any([rwo1, rwo2, rwo3, clo1, clo2, clo3, dio1, dio2]):
        fgo = 'Player o'
    if fgo or fgx:
        print(f'{fgo if fgo else fgx} is winner !!!')
        break
    elif 'p' not in r:
        print('This is Draw')
        break
    print(f'Player {"x" if h else "O"} :', end=' ')
    a = input()
