def ins(e, ls):
    yield [e, *ls]
    if ls:
        for i in ins(e, ls[1:]):
            yield [ls[0], *i]

def misterio(ls):
    if ls:
        for m in misterio(ls[1:]):
            for i in ins(ls[0], m):
                yield i
    else:
        yield []

def suspenso(ls):
    if ls:
        ms = []
        for m in suspenso(ls[1:]):
            if m is not None:
                ms.append(m)
            if (len(ms) == len(ls) - 1):
                for i in ins(ls[0], ms):
                    for j in i:
                        yield j
                ms = []
    else:
        yield None

print("Misterio...")
for m in misterio([1, 2, 3]):
    print(m)

print("Suspenso...")
for s in suspenso([1, 2, 3]):
    print(s, end = ' ')
print()
