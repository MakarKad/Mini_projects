def lst_split(a,b=[]):
    if type(a) != list:
        a = [int(i) for i in a.split()]
    if len(a) % 2 != 0:
        b += [[a.pop(0)]]
    for i in range(0,len(a),2):
        b += [[min(a[i],a[i+1]),max(a[i],a[i+1])]]
    return b


def lst_plus(a,b,c = []):
    if a == []:
        c += b
        return c
    elif b == []:
        c += a
        return c
    if a[0] == b[0]:
        c += [a.pop(0)]
    elif a[0] < b[0]:
        c += [a.pop(0)]
    else:
        c += [b.pop(0)]
    lst_plus(a,b,c)
    return c


def lst_sliv(a):
    if type(a) != list:
        a = lst_split(a)
    if len(a) > 1:
        a += [lst_plus(a.pop(-2),a.pop(-1),c=[])]
        lst_sliv(a)
    return a[0]


print(*(lst_sliv(input())))









