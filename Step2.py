a = [['1', 'Портос', '5', 'Да'], ['2', 'Арамис', '3', 'Да'], ['3', 'Атос', '4', 'Да'],
     ['4', "д'Артаньян", '2', 'Нет'], ['5', 'Балакирев', '1', 'Нет']]
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[i][j].isdigit():
            a[i][j] = int(a[i][j])

def srt(a):
    if c.index(a) == 0:
        return 3
    elif c.index(a) == 1:
        return 0
    elif c.index(a) == 2:
        return 2
    else:
        return 1

t_sorted = (('Имя','Зачет', 'Оценка','Номер'),)
for c in a:
    c = sorted(c,key = srt)
    t_sorted += ((tuple(c),))

print(t_sorted)